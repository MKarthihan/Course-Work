"""
-------------------------------------------------------
Lab 5, Task 3
(Recursively counts number of vowels in a string.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import vowel_count

# User input
s = str(input("Enter a String to examine: "))

# Call out
count = vowel_count(s)

# Display
print(f"Vowel Count: {count}")