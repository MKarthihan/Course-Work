"""
-------------------------------------------------------
Lab 6, Task 1
(Sums and returns the total of all even numbers from 2 to number)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
# Import
from functions import sum_even

# Users input
num = int(input("Enter a number:"))

# Call outs
total = sum_even(num)

# Display
print(f"The number of all even numbers from 2 to {num:d} is: {total:d}")
