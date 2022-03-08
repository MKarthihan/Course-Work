"""
-------------------------------------------------------
Lab 11, Task 6
(Statistics on a 2D list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-30"
-------------------------------------------------------
"""
# Import
from functions import stats
import random

# Matrix
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
print("")
matrix = [[random.randint(low, high) for x in range(cols)]
          for y in range(rows)]
print(matrix)

# Call out
smallest, largest, total, average = stats(matrix)

# Display
print("")
print(f"Smallest = {smallest}")
print(f"Largest = {largest}")
print(f"Total = {total}")
print(f"Average = {average:.2f}")
