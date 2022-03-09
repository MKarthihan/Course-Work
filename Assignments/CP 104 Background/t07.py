"""
-------------------------------------------------------
Assignment 1, Task 7
(Transpose the contents of matrix a)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import matrix_transpose
import random

# Matrix
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
a = [[random.randint(low, high) for x in range(cols)] for y in range(rows)]
print("")
print("Matrix:")
print(f"{a}")

# Call out
b = matrix_transpose(a)

# Display
print("")
print("Transposed matrix: ")
print(f"{b}")