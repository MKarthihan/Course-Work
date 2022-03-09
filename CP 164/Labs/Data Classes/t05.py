"""
-------------------------------------------------------
Lab 1, Task 5
(Reads a file of food strings into a list of Food objects)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from Food_utilities import read_foods

# File opening
file_variable = open("foods.txt", "r")

# Call out
foods = read_foods(file_variable)
file_variable.close()

# Display
for food in foods:
    print(food)
file_variable.close()