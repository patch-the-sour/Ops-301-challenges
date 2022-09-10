#!/usr/bin/python3

# Script: Ops 301d5 challenge 09
# Author: Graceson Langston                   
# Date of latest revision: 09/09/22      
# Purpose: 
# Assigns a variable a list of ten strings
# Prints the fourth element of the list
# Prints the sixth-tenth element of the list
# Changes the value of the seventh element to "onion"

# Assigns a variable a list of ten strings
shoppinglist = ["baked beans", "watermelons", "eggs", "avacados", "reeses", "milk", "bread", "lettuce", "chips", "hamburger"]

# Main
# Prints regular shopping list
print("Your Shopping List:")
print(shoppinglist)

# Prints the fourth element of the list
print("The 4th item on your shopping list:")
print(shoppinglist[3])

# Prints the sixth-tenth element of the list
print("The 6th through 10th item on your shopping list:")
print(shoppinglist[5:11])

# Changes the value of the seventh element to "onion"
print("The 7th item on your shopping list has changed from bread to onions!")
shoppinglist[6]= "onions"

# Prints out new shopping list items
print("Here is your new shopping list:")
print(shoppinglist)

# End
