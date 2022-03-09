"""
-------------------------------------------------------
Lab 8, Task 4
()
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# Import
from functions import generate_integer_list

# User input
n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

# Call out
values = generate_integer_list(n, low, high)

# Display
print(f"Values: {values}")
