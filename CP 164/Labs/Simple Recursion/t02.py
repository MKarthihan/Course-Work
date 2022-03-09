"""
-------------------------------------------------------
Lab 5, Task 2
(Recursively find the Greatest Common Denominator of two numbers.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import gcd

# User input
n = int(input("Enter a Integer: "))
m = int(input("Enter another Integer: "))

# Call out
ans = gcd(m,n)

# Display
print(f"Answer: {ans}")