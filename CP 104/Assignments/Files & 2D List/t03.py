"""
-------------------------------------------------------
Assignment 9, Task 3
(Evaluates the contents of a file)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-12-01"
-------------------------------------------------------
"""
# Import
from functions import file_stats

# File opening
fh = open("addresses.txt", "r", encoding="utf-8")

# Call outs
ucount, lcount, dcount, wcount = file_stats(fh)

# Display
print(f"Uppercase Letters: {ucount}")
print(f"Lowercase Letters: {lcount}")
print(f"Digits: {dcount}")
print(f"Whitesapce characters: {wcount}")
