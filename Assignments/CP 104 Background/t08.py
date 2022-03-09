"""
-------------------------------------------------------
Assignment 1, Task 8
(Determines the smallest, largest, total, and average of the values in the 2D list a)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import matrix_stats
import random

# Matrix making
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
print("")
a = [[random.randint(low, high) for x in range(cols)] for y in range(rows)]
print(a)

# Call out
small, large, total, average = matrix_stats(a)

# Display
print("")
print(f"Smallest = {small}")
print(f"Largest = {large}")
print(f"Total = {total}")
print(f"Average = {average:.2f}")