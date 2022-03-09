"""
-------------------------------------------------------
Assignment 1, Task 3 
(Analyzes the characters in a file)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import file_analyze

# File Opening
fv = open("testing.txt", "r")

# Call out
u, l, d, w, r = file_analyze(fv) 

# Display
print(f"Uppercase letters: {u}")
print(f"Lowercase letters: {l}")
print(f"Digits: {d}")
print(f"Whitespaces: {w}")
print(f"Remaning Characters: {r}")
fv.close()