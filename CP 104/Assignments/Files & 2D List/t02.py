"""
-------------------------------------------------------
Assignment 9, Task 2
(Positive integers from a file into a list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-30"
-------------------------------------------------------
"""
# Import
from functions import file_integers

# File opening
fh = open("numbers.txt", "r", encoding="utf-8")

# Call out
numbers = file_integers(fh)

# Display
print(f"{numbers}")
