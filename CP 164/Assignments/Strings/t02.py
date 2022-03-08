"""
-------------------------------------------------------
Assignment 8, Task 2
(Pluralizes a string)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-24"
-------------------------------------------------------
"""
# Import
from functions import pluralize

# Users input
string = str(input("Enter a word that can be pluralized:"))

# Call out
plural = pluralize(string)

# Display
print(f"{plural}")
