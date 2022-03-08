"""
-------------------------------------------------------
Assignment 7, Task 3
(Indexes of target in values)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import list_indexes
from random import randint

# List
values = [randint(1, 10) for i in range(randint(5, 10))]
print(values)

# User input
target = int(input("Enter a target value:"))

# Call outs
locations = list_indexes(values, target)

# Display
print(f"{locations}")
