"""
-------------------------------------------------------
Assignment 2, Task 5
(Searches for foods that fit certain conditions)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Import
from Food_utilities import food_search
from t01 import foods

# User Input
print("~"*45)
origin = int(input("Origin: "))
max_cals = int(input("Maximum Calories: "))
veg = input("Vegetarian: ")
if veg == "True":
    is_veg = True 
elif veg == "False":
    is_veg = False
else:
    is_veg = None
print()

# Call out
foods = foods
results = food_search(foods, origin, max_cals, is_veg)

# Display
for element in results:
    print()
    print(element)