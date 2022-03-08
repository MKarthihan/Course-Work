"""
-------------------------------------------------------
Lab 7, Task 9
(Value between low and high)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-04"
-------------------------------------------------------
"""
# import
from functions import get_int

# Users input
low = int(input("Enter a value for the minimum of the range:"))
high = int(input("Enter a value for the maximum of the range:"))

# Call out
value = get_int(low, high)

# Display
print(f"Value: {value:d}")
