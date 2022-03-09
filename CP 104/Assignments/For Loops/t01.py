"""
-------------------------------------------------------
Assignment 5, Task 1
(Factorial of Number)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-02"
-------------------------------------------------------
"""
# import
from functions import factorial

# Users import
num = int(input("Number to factorial:"))

# call outs
product = factorial(num)

# Display
print(f"{num:d}! = {product:d}")
