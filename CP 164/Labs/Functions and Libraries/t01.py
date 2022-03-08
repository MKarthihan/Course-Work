"""
-------------------------------------------------------
Lab 4, Task 1
(Diameter Finder)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-07"
-------------------------------------------------------
"""
# Imports
from functions import diameter

# User Input
radius = float(input("Enter radius:"))

# Call out from import
diam = diameter(radius)

# Display the diamter of circle
print(f"Diameter of circle: {diam:.2f}")
