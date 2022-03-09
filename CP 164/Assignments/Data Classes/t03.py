"""
-------------------------------------------------------
Assignment 2, Task 3
(Determines the average calories in a list of foods)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Import 
from Food_utilities import calories_by_origin
from t01 import foods

# User input
print("~"*45)
origin = int(input("Origin Number: "))

# Call out
foods = foods
a = calories_by_origin(foods, origin)


# Display
print(f"Average calories from the chosen Origin: {a}")