"""
-------------------------------------------------------
Assignment 1, Task 5 
(Determines if s is a palindrome)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import is_palindrome

# Users input
s = str(input("Enter a string: "))

# Call out
palindrome = is_palindrome(s)

# Display
print(f"Is '{s}' a palindrome?... It is {palindrome}")