"""
-------------------------------------------------------
Assignment 6, Task 2
(Determines if a number is a prime number)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-14"
-------------------------------------------------------
"""
# Import
from functions import is_prime

# Users input
num = int(input("Enter a number:"))

# Call out
prime = is_prime(num)

# Display
print(f"Is {num:d} a prime number?: {prime}")
