"""
-------------------------------------------------------
Lab 6, Task 12
(Calculates and prints a table of how much a GIC)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
# Import
from functions import gic

# Users input
value = int(input("Enter the GIC purchase value:"))
years = int(input("Enter the number of years invested:"))
rate = float(input("Enter the GIC interest rate (%):"))

# Call out
print(f" ")
gic(value, years, rate)
