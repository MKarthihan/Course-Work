"""
-------------------------------------------------------
Assignment 1, Task 9
(Converts a word to Pig Latin)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import pig_latin

# User input
word = str(input("Word: "))

# Call out
pl = pig_latin(word)

# Display
print(f"Pig Latin Word: {pl}")