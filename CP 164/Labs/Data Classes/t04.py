"""
-------------------------------------------------------
Lab 1, Task 4
(Creates and returns a food object from a line of string data)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from Food_utilities import read_food

# User Input
line = str(input("Name|Origin|Is_vegetarian|Calories: "))

# Call out
f = read_food(line)

# Display
print("")
print(f)