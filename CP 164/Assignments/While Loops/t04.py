"""
-------------------------------------------------------
Assignment 6, Task 4
(Counts the number of digits in an integer)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-14"
-------------------------------------------------------
"""
# Import
from functions import digit_count

# Users input
num = int(input("Enter a number:"))

# Call out
count = digit_count(num)

# Display
print(f"{num:d} has {count:d} integers")
