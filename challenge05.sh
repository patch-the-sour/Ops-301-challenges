#!/bin/bash

# Script Name:Clearing logs
# Author:Graceson Langston
# Date of last revision:09/05/22
# Description of purpose: Clearing system logs 

cd /var/log

# printing before contents
echo "Contents of syslog before clearing"
cat syslog
echo "Contents of wtmp before clearing"
cat wtmp

# clearing the files
cd /var/log
cat /dev/null > syslog
cat /dev/null > wtmp

# printing contents after clearing
echo "syslog after clearing"
cat syslog
echo "wtmp after clearing"
cat wtmp
echo "Good Bye."
