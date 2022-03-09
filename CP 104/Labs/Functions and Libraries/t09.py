"""
-------------------------------------------------------
Lab 4, Task 9
(Product of fractions)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-07"
-------------------------------------------------------
"""
# Import
from functions import fraction_product

# Users input
num1 = int(input("Enter numerator of fraction 1:"))
den1 = int(input("Enter denominator of fraction 1:"))
num2 = int(input("Enter numerator of fraction 2:"))
den2 = int(input("Enter denominator of fraction 2:"))

# Call out from import
num = fraction_product(num1, den1, num2, den2)
den = fraction_product(num1, den1, num2, den2)
product = fraction_product(num1, den1, num2, den2)

# Display
print(f"Product = {num[0]}/{den[1]}")
print(f"Decimal = {product[2]:.2f}")
