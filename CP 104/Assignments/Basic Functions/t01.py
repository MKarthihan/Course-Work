"""
-------------------------------------------------------
Assignment 3, Task 1
(Feet to Acres)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-11"
-------------------------------------------------------
"""
# Import
from functions import feet_to_acres

# Users inputs
square_footage = float(input("Square footage:"))

# Call outs from import
acres = feet_to_acres(square_footage)

# Display the acres and square footage
print(f"{acres:.2f} acres is equivalent to {square_footage:,.2f} square feet")
