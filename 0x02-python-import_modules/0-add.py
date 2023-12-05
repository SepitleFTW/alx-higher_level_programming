#!/usr/bin/python3

def add(a, b):

# Assigning values to variables
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import add

# Printing the result using string formatting
print("{} + {} = {}".format(a, b, add(a, b)))

