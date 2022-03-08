"""
-------------------------------------------------------
Assignment 8, Task 1
(New string with added space between words)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-24"
-------------------------------------------------------
"""
# Import
from functions import add_spaces

# Users input
string = str(input("Enter a string:"))

# Call out
new_string = add_spaces(string)

# Display
print(f"{new_string}")
