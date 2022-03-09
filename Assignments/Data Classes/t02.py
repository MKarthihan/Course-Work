"""
-------------------------------------------------------
Assignment 2, Task 2
(Determines the average calories in a list of foods.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Import
from Food_utilities import average_calories
from t01 import foods

# Call out
foods = foods
avg = average_calories(foods)

# Display
print("~"*45)
print(f"Average Calories: {avg}")
