"""
-------------------------------------------------------
Lab 11, Task 1
(Generates a 2D list of numbers of the given type)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-29"
-------------------------------------------------------
"""
# Import
from functions import generate_matrix_num

# Users input
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
low = int(input("Low value: "))
high = int(input("High value: "))
value_type = str(input("Type of values: "))

# Call outs
matrix = generate_matrix_num(rows, cols, low, high, value_type)

# Display
print("")
print(f"{matrix}")
