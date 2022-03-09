"""
-------------------------------------------------------
Assignment 2, Task 1
(Creates a list of foods by origin)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Import
from Food import Food
from Food_utilities import by_origin, read_foods

# File opening
file_variable = open("foods.txt", "r")
foods = read_foods(file_variable)
file_variable.close()

# Display
for origin in range(len(Food.ORIGIN)):
    v = by_origin(foods, origin)
    print(f"Origin:     {Food.ORIGIN[origin]}")
    print()
    for x in v:
        print(x)
    print()