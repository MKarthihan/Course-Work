"""
-------------------------------------------------------
Lab 1, Task 6
(Writes a list of food objects to a file)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from Food_utilities import write_foods
from t05 import foods

# File opening
file_variable = open("new_foods.txt", "w")

# Call out
write_foods(file_variable, foods)
file_variable.close()

