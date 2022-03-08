"""
-------------------------------------------------------
Assignment 9, Task 6
(Reads a addresses from fh into a list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-12-01"
-------------------------------------------------------
"""
# Import
from functions import get_addresses

# File opening
fh = fh = open("addresses.txt", "r", encoding="utf-8")

# Call out
addresses = get_addresses(fh)

# Display
print(f"{addresses}")
