"""
-------------------------------------------------------
Lab 11, Task 2
(Generates a 2D list of random lower case letter)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-29"
-------------------------------------------------------
"""
# Import
from functions import generate_matrix_char

# Users input
rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

# Call out
matrix = generate_matrix_char(rows, cols)

# Display
print(" ")
print("Matrix of characters:")
print(" ")
print(f"{matrix}")
