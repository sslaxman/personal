#!/bin/bash

curDir=`pwd`

#Channel-Capture
mkdir $curDir/prof1; cd $curDir/prof1; /home/admin/udpCapture 235.100.101.28 10001 eth0&
mkdir $curDir/prof2; cd $curDir/prof2; /home/admin/udpCapture 235.100.101.28 10002 eth0&
mkdir $curDir/prof3; cd $curDir/prof3; /home/admin/udpCapture 235.100.101.28 10003 eth0&
mkdir $curDir/prof4; cd $curDir/prof4; /home/admin/udpCapture 235.100.101.28 10004 eth0&
mkdir $curDir/prof5; cd $curDir/prof5; /home/admin/udpCapture 235.100.101.28 10005 eth0&
mkdir $curDir/prof6; cd $curDir/prof6; /home/admin/udpCapture 235.100.101.28 10006 eth0&
mkdir $curDir/prof7; cd $curDir/prof7; /home/admin/udpCapture 235.100.101.28 10007 eth0&
