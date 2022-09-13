#!/usr/bin/python3

# Script: Ops301d5 challenge 10
# Author:Graceson Langston                   
# Date of latest revision: 9/12/22      

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# Compare Two Values
a = input("Please input a random number for variable a: ")
b = input("Please input a random number for variable b: ")

# Turns input into an interger
int(a)
int(b)

# Main

# Conditional
if a == b:
    print("a equals b")
else:
    print("a does not equal b")

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
elif a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than or equal to b")

# End
