"""
-------------------------------------------------------
Lab 9, Task 12
(Replaces all the commas with a period)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import comma_period_replace

# User input
s = str(input("Enter a string:"))

# Call out
out = comma_period_replace(s)

# Display
print(f"{out:s}")
