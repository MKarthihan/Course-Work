"""
-------------------------------------------------------
Assignment 3, Task 4
(Multiplication of two fractions)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-11"
-------------------------------------------------------
"""
# Import
from functions import multiply_fractions

# Users input
num1 = int(input("Numerator 1:"))
denom1 = int(input("Denominator 1:"))
num2 = int(input("Numerator 2:"))
denom2 = int(input("Denominator 2:"))

# Call outs from import
numerator = multiply_fractions(num1, denom1, num2, denom2)
denominator = multiply_fractions(num1, denom1, num2, denom2)
product = multiply_fractions(num1, denom1, num2, denom2)

# Display result
print(f"Result: {numerator[0]:d}/{denominator[1]:d} = {product[2]:.3f}")
