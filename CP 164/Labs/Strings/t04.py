"""
-------------------------------------------------------
Lab 9, Task 4
(Product code and whether the various parts are valid)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import validate_code

# Users input
product_code = str(input("Enter a product code:"))

# Display
validate_code(product_code)
