//
// precise-generator.h
//
//  Created by Peter Gusev on 19 March 2016.
//  Copyright 2013-2016 Regents of the University of California
//

#ifndef __precise_generator_h__
#define __precise_generator_h__

#include <iostream>
#include <boost/asio.hpp>

#if BOOST_ASIO_HAS_STD_CHRONO

#include <functional>
#include <chrono>

namespace lib_bind = std;
namespace lib_fun = std;
namespace lib_chrono = std::chrono;
#define arg_placeholder_1 std::placeholders::_1

#else

namespace lib_bind = boost;
namespace lib_fun = boost;
namespace lib_chrono = boost::chrono;
#define arg_placeholder_1 boost::arg<1>()

#endif

//******************************************************************************

class PreciseGeneratorImpl;

class PreciseGenerator
{
  public:
    typedef lib_fun::function<void()> Task;
    PreciseGenerator(boost::asio::io_service &io, const double &ratePerSec,
                     const Task &task);
    ~PreciseGenerator();

    void start();
    void stop();
    bool isRunning();
    long long getFireCount();
    double getMeanProcessingOverheadNs();
    double getMeanTaskTimeNs();

  private:
    std::shared_ptr<PreciseGeneratorImpl> pimpl_;
};

#endif
