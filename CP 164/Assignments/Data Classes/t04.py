"""
-------------------------------------------------------
Assignment 2, Task 4
(Prints a formatted table of foods, sorted by name)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Import 
from Food_utilities import food_table
from t01 import foods

# Call out
foods = foods
print("~"*45)
food_table(foods)