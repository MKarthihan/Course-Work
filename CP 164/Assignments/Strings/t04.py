"""
-------------------------------------------------------
Assignment 8, Task 4
(ISBN string is valid)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# Import
from functions import is_valid_isbn

# Users input
isbn = str(input("Enter a ISBN code:"))

# Call out
valid = is_valid_isbn(isbn)

# Display
if valid == True:
    print(f"'{isbn}' is a valid ISBN code.")
elif valid == False:
    print(f"'{isbn}' is not a valid ISBN code.")
