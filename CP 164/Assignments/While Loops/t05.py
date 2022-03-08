"""
-------------------------------------------------------
Assignment 6, Task 5
(The sum of factors of an integer not including
 the integer itself)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-14"
-------------------------------------------------------
"""
# Import
from functions import sum_factors

# Users input
num = int(input("Enter a number:"))

# Call out
total = sum_factors(num)

# Display
print(f"The factors of {num} added is equal to {total:.0f}")
