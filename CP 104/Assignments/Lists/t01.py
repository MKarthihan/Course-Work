"""
-------------------------------------------------------
Assignment 7, Task 1
(List factors that make up that number)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import list_factors

# Users input
num = int(input("Enter a number:"))

# Call outs
factor_list = list_factors(num)

# Display
print(f"The factors of {num:d} is {factor_list}")
