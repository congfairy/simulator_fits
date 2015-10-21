#!/bin/bash
./extracttrace --log=replay.thres:verbose --cfg=surf/precision:1e-9 $1/one_host_one_disk.xml cluefs-centos7-lsst_stack_demo-11.0_deployment.xml cluefs-centos7-lsst_stack_demo-11.0_action_trace.txt sleep >& $1/logsleep
