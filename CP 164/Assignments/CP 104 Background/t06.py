"""
-------------------------------------------------------
Assignment 1, Task 6
(Returns maximum absolute difference between adjacent values in a list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import 
from functions import max_diff
import random

# List
a = random.sample(range(0, 100), 5)
print(a)

# Call out
md = max_diff(a)

# Display
print(f"Maximum absolute difference: {md}")