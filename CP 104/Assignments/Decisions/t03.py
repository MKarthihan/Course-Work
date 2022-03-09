"""
-------------------------------------------------------
Assignment 4, Task 3
(Product of the two largest values)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Import
from functions import product_largest

# User input
v1 = float(input("Enter a number:"))
v2 = float(input("Enter a second number:"))
v3 = float(input("Enter a third number:"))

# Call out
product = product_largest(v1, v2, v3)

# Display
print(
    f"The product of the two largest values of {v1:.0f}, {v2:.0f}, and {v3:.0f} is {product:.0f}")
