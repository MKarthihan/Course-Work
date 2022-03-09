"""
-------------------------------------------------------
Assignment 9, Task 1
(Prints first linecount lines of fh)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""
# Import
from functions import file_head

# File Opening
fh = open("functions.py", "r", encoding="utf-8")

# Users input
linecount = int(input("Enter number of lines: "))

# Display
file_head(fh, linecount)
