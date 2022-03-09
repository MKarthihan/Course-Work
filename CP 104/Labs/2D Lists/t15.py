"""
-------------------------------------------------------
Lab 11, Task 15
(Compares two matrices to see if they are equal)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-29"
-------------------------------------------------------
"""
# Input
from functions import matrix_equal
import random
import string

# Matrix 1 & 2
type1 = str(input("Enter type (str) or (int) or (float) :"))
rows1 = int(input("Number of rows: "))
cols1 = int(input("Number of columns: "))
rows2 = int(input("Number of rows: "))
cols2 = int(input("Number of columns: "))
print("")
if type1 == "str":
    lowercase = string.ascii_letters
    matrix1 = [[random.choice(lowercase.lower())
                for x in range(cols1)]for y in range(rows1)]
    matrix2 = [[random.choice(lowercase.lower())
                for x in range(cols2)]for y in range(rows2)]
    print("First matrix:")
    print(matrix1)
    print("")
    print("Second matrix:")
    print(matrix2)
elif type1 == "int":
    low1 = int(input("Low value: "))
    high1 = int(input("High value: "))
    low2 = int(input("Low value: "))
    high2 = int(input("High value: "))
    matrix1 = [[random.randint(low1, high1)
                for x in range(cols1)] for y in range(rows1)]
    matrix2 = [[random.randint(low2, high2)
                for x in range(cols2)] for y in range(rows2)]
    print("First matrix:")
    print(matrix1)
    print("")
    print("Second matrix:")
    print(matrix2)
elif type1 == "float":
    low1 = int(input("Low value: "))
    high1 = int(input("High value: "))
    low2 = int(input("Low value: "))
    high2 = int(input("High value: "))
    matrix1 = [[random.uniform(low1, high1)
                for x in range(cols1)] for y in range(rows1)]
    matrix2 = [[random.uniform(low2, high2)
                for x in range(cols2)] for y in range(rows2)]
    print("First matrix:")
    print(matrix1)
    print("")
    print("Second matrix:")
    print(matrix2)

# Call out
equal = matrix_equal(matrix1, matrix2)

# Display
print("")
print(f"Equal matrices: {equal}")
