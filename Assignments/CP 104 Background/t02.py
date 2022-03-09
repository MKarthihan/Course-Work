"""
-------------------------------------------------------
Assignment 1, Task 2
(Disemvowels a string)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import dsmvwl

# Users input
s = str(input("Enter a sentence:"))

# Call out
out = dsmvwl(s)

# Display
print(f"Sentence: {s}")
print(f"Disemvowelled: {out}")