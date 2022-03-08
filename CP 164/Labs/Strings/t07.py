"""
-------------------------------------------------------
Lab 9, Task 7
(Counts the number of vowels in a string)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import vowel_count

# Users
s = str(input("Enter a string:"))

# Call out
count = vowel_count(s)

# Display
print(f"There are {count:d} vowels.")
