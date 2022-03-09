"""
-------------------------------------------------------
Assignment 5, Task 5
(Sum of x values starting from y with an increment of z)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-07"
-------------------------------------------------------
"""
# import
from functions import range_total

# Users input
start = int(input("Start value:"))
increment = int(input("Increment range value:"))
count = int(input("Number of values:"))

# Call out
total = range_total(start, increment, count)

# Display
print(
    f"The sum of {count:d} values starting from {start:d} with an increment of {increment:d} is: {total:d}")
