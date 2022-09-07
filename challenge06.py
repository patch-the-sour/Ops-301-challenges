#! /bin/python3


# Script: Bash in Python
# Author: Graceson Langston                    
# Date of latest revision:  9/6/22    
# Purpose: Using Python to execute Bash commands

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# The Python function print() must be used at least three times
# If you don’t have access to your hardware spec-fetching bash script, include the following bash commands inside a Python script:

# whoami
# ip a
# lshw -short

# imports the os library
import os
# variables
who_am_i_var="whoami"
ip_a_var="ip a"
lshw_short_var="lshw -short"
# prints a label and the outcome of the system method
print ("User information:", os.system(who_am_i_var))
print("IP address:", os.system(ip_a_var))
print("Hardware information:", os.system(lshw_short_var))
