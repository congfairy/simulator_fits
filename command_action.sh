#!/bin/bash
./extracttrace --log=replay.thres:verbose --cfg=surf/precision:1e-9 $1/one_host_one_disk.xml lsst-demo-v10.1-ubuntu-v14.04-cluefs_deployment.xml lsst-demo-v10.1-ubuntu-v14.04-cluefs_action_trace.txt action >& $1/logaction
