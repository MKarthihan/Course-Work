"""
-------------------------------------------------------
Assignment 8, Task 3
(Longest common ending of two strings)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-24"
-------------------------------------------------------
"""
# Import
from functions import common_ending

# User input
string1 = str(input("Enter a word: "))
string2 = str(input("Enter another word: "))

# Call outs
common = common_ending(string1, string2)

# Display
print(f"{common}")
