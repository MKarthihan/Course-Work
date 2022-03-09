"""
-------------------------------------------------------
Assignment 9, Task 5
(2D matrix rotated to the right)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""
# Import
from functions import matrix_rotate_right
import random

# Matrix
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
matrix = [[random.randint(low, high) for x in range(cols)]
          for y in range(rows)]
print("")
print("Matrix:")
print(f"{matrix}")

# Call out
rotated = matrix_rotate_right(matrix)

# Display
print("")
print("Rotated to:")
print(f"{rotated}")
