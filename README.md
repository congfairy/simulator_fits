# storage-simulator - a tool for simulating the storage system  using the simgrid API and the trace file  got by cluefs.

## Overview
'storage-simulator' is a simulator which simulating the function of the storage system ,using the data got for LSST(Large Synoptic Survey Telescope) by clusfs ,it is fulfilled according to the simgrid ,most of the api is provided by simgrid ,and we use the trace replay function to fulfill our target.

## Motivation
The main goal of developing the utility is to using the data got from LSST to simulator the storage system ,changing the development file to see which parameter affects the  performance of the storage system most and then we can optimize the storage system of LSST.

### How to use
*  Download and install simgrid as:http://simgrid.gforge.inria.fr/simgrid/3.12/doc/install.html
*  Use configure.sh to produce configuration files(filename_deployment.xml,filename_action_trace.txt,storage_content.txt,filename_csvtime.txt) with the command:./configure.sh filename.csv
*  17745.csv is a sample trace file which you can use to test your simulator.
*  Compile the program with the command "make"
*  command_action.sh is a shell script with the command to run the simulator which really works with some action with the trace file:lsst-demo-v10.1-ubuntu-v14.04-cluefs.csv 
   command_sample_action.sh is a shell script with the command to run the simulator which really works with some action with the trace file:17745.csv 
   command_sample_sleep.sh is a shell script with the command to run the simulator with sleeping function for the trace file:17745.csv 
   command_sleep.sh is a shell script with the command to run the simulator with sleeping function for the trace file:lsst-demo-v10.1-ubuntu-v14.04-cluefs.csv
* The format of directory 30_100_120_200 is Write-bandwidth(slow)_Read-bandwidth(slow)_Write-bandwidth(fast)_Read-bandwidth(fast).In the directory,there  is the platform.xml which correspond to the parameters.
* When you want to run the program , use the command:
 e.g: ./command_action.sh 30_100_120_200
Then you will find the result: logaction file in the directory 30_100_120_200.Then you can check the log and find something useful.

### Explanation of the command and the files
for example: in the command_action.sh file ,there is the following command
:./extracttrace --log=replay.thres:verbose --cfg=surf/precision:1e-9 $1/one_host_one_disk.xml lsst-demo-v10.1-ubuntu-v14.04-cluefs_deployment.xml lsst-demo-v10.1-ubuntu-v14.04-cluefs_action_trace.txt action >& $1/logaction

 * platform.xml:In order to run any simulation, SimGrid must be provided with three things: something to run (i.e., your code), a description of the platform on which you want to simulate your application and lastly information about the deployment process.http://simgrid.gforge.inria.fr/simgrid/3.12/doc/platform.html
 
 * deployment.xml:When using SimGrid, you basically need your user code, a platform description, and something allowing to map your (simulated) process on your (simulated) platform. This is what deployment file is all about.So deployment file just consists of saying which process runs where and which arguments it should take as input.http://simgrid.gforge.inria.fr/simgrid/3.12/doc/deployment.html
 
 * action_trace.txt:It describes the actions that each process executes.It is needed when simgrid replay the trace.
    The format of this file is :
    pid,action,filepath,duration,openid(open,read,write,flush,release,creat,readdir),position(read,write),bytereq(read,write)
     
 * storage_content.txt:It describes the initial state of the storage disk.
    The format of this file is:filepath,filesize
    This file is used in the platform.xml .

 * action(sleep):It is a parameter to decide which action you want your simulator to do.

### verify the simulator
* 1.When you use the command :./configure.sh filename.csv
   It will produce the file filename_csvtime.xml which shows the start and end time of every process according to the .csv trace file.

* 2.After you run the simulator.You can use the script logtime.sh to parsing your logaction or logsleep with the command:./logtime.sh logaction.It will produce the file logaction_logtime.xml in the same directory of logaction.Then you can compare the file filename_csvtime.xml with logaction_logtime.xml in detail and decide whether the result is right.

### What is on going 
Now is on going with changing the configuration of the storage.xml such as the parameter of the disk ,to see the change of time and then draw it on the plot as a curve to describe the time changes with the change of the disk parameter.




