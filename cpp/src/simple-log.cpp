//
//  simple-log.cpp
//  ndnrtc
//
//  Copyright 2013 Regents of the University of California
//  For licensing details see the LICENSE file.
//
//  Author:  Peter Gusev
//  Created: 8/8/13
//

#include <boost/chrono.hpp>
#include <boost/thread.hpp>
#include <boost/asio.hpp>

#include <sys/time.h>
#include <mach/mach_time.h>
#include <fstream>
#include <iomanip>
#include "simple-log.h"

#define MAX_BUF_SIZE 4*256 // string buffer

using namespace ndnlog;
using namespace new_api;

static char tempBuf[MAX_BUF_SIZE];
static std::string lvlToString[] = {
    [NdnLoggerLevelTrace] =     "TRACE",
    [NdnLoggerLevelDebug] =     "DEBUG",
    [NdnLoggerLevelInfo] =      "INFO ",
    [NdnLoggerLevelWarning] =   "WARN ",
    [NdnLoggerLevelError] =     "ERROR",
    [NdnLoggerLevelStat] =      "STAT "
};

boost::asio::io_service LogIoService;
boost::thread LogThread;
boost::shared_ptr<boost::asio::io_service::work> LogThreadWork;

ndnlog::new_api::NilLogger ndnlog::new_api::NilLogger::nilLogger_;
ndnlog::new_api::Logger* Logger::sharedInstance_ = 0;

void startLogThread();
void stopLogThread();

//******************************************************************************
pthread_mutex_t new_api::Logger::stdOutMutex_ = PTHREAD_RECURSIVE_MUTEX_INITIALIZER;
std::map<std::string, new_api::Logger*> new_api::Logger::loggers_;

unsigned int new_api::Logger::FlushIntervalMs = 100;

#pragma mark - construction/destruction
new_api::Logger::Logger(const NdnLoggerDetailLevel& logLevel,
                        const std::string& logFile):
isWritingLogEntry_(false),
currentEntryLogType_(NdnLoggerLevelTrace),
logLevel_(logLevel),
logFile_(logFile),
outStream_(&std::cout),
isStdOutActive_(true),
logMutex_((pthread_mutex_t)PTHREAD_RECURSIVE_MUTEX_INITIALIZER)
{
    if (logFile_ != "")
    {
        isStdOutActive_ = false;
        outStream_ = new std::ofstream();
        getOutFileStream().open(logFile_.c_str(),
                                std::ofstream::out | std::ofstream::trunc);
        lastFlushTimestampMs_ = getMillisecondTimestamp();
    }
    
    isProcessing_ = true;
}

new_api::Logger::~Logger()
{
    isProcessing_ = false;
}

//******************************************************************************
#pragma mark - public
new_api::Logger&
new_api::Logger::log(const NdnLogType& logType,
                     const ndnlog::new_api::ILoggingObject* loggingInstance,
                     const std::string& locationFile,
                     const int& locationLine)
{
    
    if (logType < (NdnLogType)logLevel_)
        return NilLogger::get();
    
    lockStreamExclusively();
    
    if (isWritingLogEntry_ &&
        currentEntryLogType_ >= (NdnLogType)logLevel_)
        *this << std::endl;
    
    unlockStream();
    
    bool shouldIgnore = (loggingInstance != 0 &&
                            !loggingInstance->isLoggingEnabled());
    
    if (!shouldIgnore &&
        logType >= (NdnLogType)logLevel_)
    {
        lockStreamExclusively();
        startLogRecord();
        
        isWritingLogEntry_ = true;
        currentEntryLogType_ = logType;
        
        // LogEntry header has the following format:
        // <timestamp> <log_level> - <logging_instance> [<location_file>:<location_line>] ":"
        // log location info is enabled only for debug levels less than INFO
        currentLogRecord_ << getMillisecondTimestamp() << "\t[" << stringify(logType) << "]";
        
        if (loggingInstance)
            currentLogRecord_
            << "[" << std::setw(25) << loggingInstance->getDescription() << "]-"
            << std::hex << std::setw(15) << loggingInstance << std::dec;
        
//        if (logType < (NdnLogType)NdnLoggerLevelDebug &&
//            locationFile != "" &&
//            locationLine >= 0)
//            getOutStream() << "(" << locationFile << ":" << locationLine << ")";
        
        currentLogRecord_ << ": ";
    }
    
    return *this;
}

void
new_api::Logger::flush()
{
    getOutStream().flush();    
}

//******************************************************************************
#pragma mark - static
void
new_api::Logger::initAsyncLogging()
{
    startLogThread();
}

void
new_api::Logger::releaseAsyncLogging()
{
    stopLogThread();
}

new_api::Logger&
new_api::Logger::getLogger(const std::string &logFile)
{
    std::map<std::string, Logger*>::iterator it = loggers_.find(logFile);
    Logger *logger;
    
    if (it == loggers_.end())
    {
        logger = new Logger(NdnLoggerDetailLevelAll, logFile);
        loggers_[logFile] = logger;
    }
    else
        logger = it->second;
    
    return *logger;
}

void
new_api::Logger::destroyLogger(const std::string &logFile)
{
    std::map<std::string, Logger*>::iterator it = loggers_.find(logFile);
    
    if (it != loggers_.end())
        delete it->second;
}

//******************************************************************************
#pragma mark - private
std::string
new_api::Logger::stringify(NdnLoggerLevel lvl)
{
    return lvlToString[lvl];
}

int64_t
new_api::Logger::getMillisecondTimestamp()
{
#if 0
    struct timeval tv;
    gettimeofday(&tv, NULL);
    
    int64_t ticks = 1000LL*static_cast<int64_t>(tv.tv_sec)+static_cast<int64_t>(tv.tv_usec)/1000LL;
    
    return ticks;
#endif
    
    struct timeval tv;
    gettimeofday(&tv, NULL);
    
    int64_t ticks = 0;
    
#if 0
    ticks = 1000LL*static_cast<int64_t>(tv.tv_sec)+static_cast<int64_t>(tv.tv_usec)/1000LL;
#else
    static mach_timebase_info_data_t timebase;
    if (timebase.denom == 0) {
        // Get the timebase if this is the first time we run.
        // Recommended by Apple's QA1398.
        kern_return_t retval = mach_timebase_info(&timebase);
        if (retval != KERN_SUCCESS) {
            // TODO(wu): Implement CHECK similar to chrome for all the platforms.
            // Then replace this with a CHECK(retval == KERN_SUCCESS);
            asm("int3");
        }
    }
    // Use timebase to convert absolute time tick units into nanoseconds.
    ticks = mach_absolute_time() * timebase.numer / timebase.denom;
    ticks /= 1000000LL;
#endif
    
    return ticks;
}

void
new_api::Logger::processLogRecords()
{
    if (isProcessing_)
    {
        bool queueEmpty = false;
        std::string record;
        
        while (recordsQueue_.pop(record))
            getOutFileStream() << record;
        
        if (&getOutStream() != &std::cout)
        {
            if ((getMillisecondTimestamp() - lastFlushTimestampMs_) >= FlushIntervalMs)
                flush();
        }
    }
    else
    {
        if (&getOutStream() != &std::cout)
        {
            getOutFileStream().flush();
            getOutFileStream().close();
        }
    }
}

void
new_api::Logger::startLogRecord()
{
    currentLogRecord_.str( std::string() );
    currentLogRecord_.clear();
}

void
new_api::Logger::finalizeLogRecord()
{
    if (!recordsQueue_.push(currentLogRecord_.str()))
        getOutFileStream() << "[CRITICAL]\tlog queue is full" << std::endl;
    else
        LogIoService.post(boost::bind(&new_api::Logger::processLogRecords, this));
}

//******************************************************************************
//******************************************************************************
ILoggingObject::ILoggingObject(const NdnLoggerDetailLevel& logLevel,
                               const std::string& logFile):
logger_(new Logger(logLevel, logFile)),
isLoggerCreated_(true){
}

void
ILoggingObject::setLogger(ndnlog::new_api::Logger *logger)
{
    if (logger_ && isLoggerCreated_)
        delete logger_;
    
    isLoggerCreated_ = false;
    logger_ = logger;
}

//******************************************************************************
void startLogThread()
{
    if (!LogThreadWork.get() &&
        LogThread.get_id() == boost::thread::id())
    {
        LogThreadWork.reset(new boost::asio::io_service::work(LogIoService));
        LogThread = boost::thread([](){
            LogIoService.run();
        });
    }
}

void stopLogThread()
{
    if (LogThreadWork.get())
    {
        LogThreadWork.reset();
        LogIoService.stop();
        LogThread.try_join_for(boost::chrono::milliseconds(100));
    }
}

