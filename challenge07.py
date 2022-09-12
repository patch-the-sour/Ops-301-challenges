#!/bin/python3
# Script: Ops 301d5-07 Directory Creation
# Author: Graceson Langston                    
# Date of latest revision:  9/7/22    
# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
# Import libraries

import os

# Declaration of variables

### Read user input here into a variable
fpath = input("Enter file path now:")
# Declaration of functions
  
### Declare a function here
def walkem(fpath):
    for (root, dirs, files) in os.walk(fpath):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main
# fpath = input("Enter file path now:")
walkem(fpath)
### Pass the variable into the function here

# End
