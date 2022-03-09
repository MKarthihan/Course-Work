"""
-------------------------------------------------------
Assignment 9, Task 4
(Flatten the contents of 2D list matrix)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-30"
-------------------------------------------------------
"""
# Import
from functions import flatten
import random

# Matrix
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
matrix = [[random.randint(low, high) for x in range(cols)]
          for y in range(rows)]
print("")
print(f"2D List: {matrix}")

# Call out
flat = flatten(matrix)

# Display
print("")
print(f"New 1D list: {flat}")
