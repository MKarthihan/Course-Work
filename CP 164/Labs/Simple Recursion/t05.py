"""
-------------------------------------------------------
Lab 5, Task 5
(Recursively determines if s is a palindrome)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import is_palindrome

# User input
s = str(input("Enter a String: "))

# Call out
palindrome = is_palindrome(s)

# Display
print(f"Verdict: {palindrome}")