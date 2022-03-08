"""
-------------------------------------------------------
Lab 5, Task 4
(Closest value)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-18"
-------------------------------------------------------
"""
# Import
from functions import closest
# User inputs
target = float(input("Enter target:"))
v1 = float(input("Enter v1:"))
v2 = float(input("Enter v2:"))

# Call outs from import
result = closest(target, v1, v2)

# Display
print(f"Closest value to {target:.1f} is {result:.1f}")
