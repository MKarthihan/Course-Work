"""
-------------------------------------------------------
Assignment 3, Task 6
(Reroutes values in a list according to a operating string and returns a new list of values)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Import 
from functions import reroute

# User input
opstring = input("Enter a String containing only 'S' and 'X's: ")

# List
values_in = [1,2,3,4,5]

# Call out
values_out = reroute(opstring, values_in)

# Display
print(values_out)