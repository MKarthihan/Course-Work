"""
-------------------------------------------------------
Assignment 7, Task 4
(Updates the list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-17"
-------------------------------------------------------
"""
# Import
from functions import subtract_lists
from random import randint

# List
minuend = [randint(1, 10) for i in range(randint(5, 10))]
print(minuend)

subtrahend = []
value = int(input("Enter number of elements : "))
for i in range(0, value):
    count = 0
    count = count + i
    elements = int(input(f"Index {count}:"))
    subtrahend.append(elements)
print(subtrahend)

# Call out
subtract_lists(minuend, subtrahend)

# Display
print(f"minuend after: {minuend}")
