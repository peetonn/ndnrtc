//
//  av-sync.cpp
//  ndnrtc
//
//  Created by Peter Gusev on 1/17/14.
//  Copyright (c) 2014 Peter Gusev. All rights reserved.
//

#include "av-sync.h"

using namespace webrtc;
using namespace ndnrtc;

#define SYNC_INIT(name) ({*CriticalSectionWrapper::CreateCriticalSection(), \
name, -1, -1, -1, -1, -1, -1})

//******************************************************************************
#pragma mark - construction/destruction
AudioVideoSynchronizer::AudioVideoSynchronizer() :
syncCs_(*CriticalSectionWrapper::CreateCriticalSection()),
audioSyncData_("audio"),
videoSyncData_("video")
{
}

//******************************************************************************
#pragma mark - public
int AudioVideoSynchronizer::synchronizePacket(FrameBuffer::Slot *slot,
                                              int64_t packetTsLocal)
{
    if (slot->isAudioPacket())
        return syncPacket(audioSyncData_, videoSyncData_,
                          slot->getPacketTimestamp(), packetTsLocal);
    
    if (slot->isVideoPacket())
        return syncPacket(videoSyncData_, audioSyncData_,
                          slot->getPacketTimestamp(), packetTsLocal);
    
    return 0;
}

void AudioVideoSynchronizer::reset()
{
    audioSyncData_.reset();
    videoSyncData_.reset();
    
    syncCs_.Enter();
    initialized_ = false;
    syncCs_.Leave();
}

//******************************************************************************
#pragma mark - private
int AudioVideoSynchronizer::syncPacket(SyncStruct& syncData,
                                       SyncStruct& pairedSyncData,
                                       int64_t packetTsRemote,
                                       int64_t packetTsLocal)
{
    CriticalSectionScoped scopedCs(&syncCs_);
 
    syncData.cs_.Enter();
    
    TRACE("[SYNC] %s: synchronizing packet %ld (%ld)",
              syncData.name_, packetTsRemote, packetTsLocal);
    
    // check if it's a first call
    if (syncData.lastPacketTsLocal_ < 0)
        initialize(syncData, packetTsRemote, packetTsLocal);
    
    syncData.lastPacketTsLocal_ = packetTsLocal;
    syncData.lastPacketTsRemote_ = packetTsRemote;
    
    int drift = 0;
    
    if (initialized_)
    {
        CriticalSectionScoped scopedCs(&pairedSyncData.cs_);
        
        int64_t hitTime = packetTsLocal;
        
        // check with the paired stream - whether it's keeping up or not
        // 1. calcualte difference between remote and local timelines for the
        // paired stream
        int pairedD = pairedSyncData.lastPacketTsRemote_ - pairedSyncData.lastPacketTsLocal_;
        TRACE("[SYNC] %s: paired D is: %d", syncData.name_, pairedD);
        
        // 2. calculate hit time in remote's timeline of the paired stream
        int64_t hitTimeRemotePaired = hitTime + pairedD;
        TRACE("[SYNC] %s: hit remote is %d", syncData.name_, hitTimeRemotePaired);
        
        // 3. calculate drift by comparing remote times of the current stream
        // and hit time of the paired stream
        drift = syncData.lastPacketTsRemote_-hitTimeRemotePaired;
        TRACE("[SYNC] %s: drift is %d", syncData.name_, drift);
        
        if (drift > TolerableDriftMs)
            DBG("[SYNC] %s: adjusting %s stream for %d", syncData.name_,
                pairedSyncData.name_, drift);
        else
            drift = 0;
    } // critical section
    
    syncData.cs_.Leave();
    
    return drift;
}

// should be called from thread-safe place
void AudioVideoSynchronizer::initialize(SyncStruct &syncData,
                                        int64_t firstPacketTsRemote,
                                        int64_t localTimestamp)
{
    TRACE("[SYNC] %s: initalize", syncData.name_);
    
    syncData.initialized_ = true;
    initialized_ = audioSyncData_.initialized_ && videoSyncData_.initialized_;
    
    syncData.lastPacketTsLocal_ = localTimestamp;
    syncData.lastPacketTsRemote_ = firstPacketTsRemote;
}
