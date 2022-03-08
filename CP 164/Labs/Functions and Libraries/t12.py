"""
-------------------------------------------------------
Lab 4, Task 12
(Converts temperatures in celsius to fahrenheit)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-07"
-------------------------------------------------------
"""
# Import
from functions import c_to_f

# Users Input
celsius = float(input("Enter a temperature (c):"))

# Call out from Import
fahrenheit = c_to_f(celsius)

# Display
print(f"{celsius} C = {fahrenheit} F ")
