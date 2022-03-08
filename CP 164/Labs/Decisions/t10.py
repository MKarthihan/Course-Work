"""
-------------------------------------------------------
Lab 5, Task 10
(Earthquake intensity)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Imports
from functions import richter

# Users input
intensity = float(input("Richter Scale Number:"))

# Call outs
result = richter(intensity)

# Display
print(f"{result:s}")
