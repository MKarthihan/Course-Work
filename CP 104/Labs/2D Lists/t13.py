"""
-------------------------------------------------------
Lab 11, Task 13
(Update matrix by multiplying each element)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-30"
-------------------------------------------------------
"""
# Import
from functions import scalar_multiply
import random

# Matrix
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
matrix = [[random.randint(low, high) for x in range(cols)]
          for y in range(rows)]
print("")
print("Matrix before scalar multiplication:")
print(matrix)

# User input
num = int(input("Enter number: "))

# Display
output = scalar_multiply(matrix, num)
print("")
print("Matrix after scalar multiplication: ")
print(f"{matrix}")
