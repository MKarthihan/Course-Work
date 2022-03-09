"""
-------------------------------------------------------
Lab 1, Task 7
(Creates a list of vegetarian foods)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import 
from Food_utilities import get_vegetarian
from t05 import foods

# Call out
v = get_vegetarian(foods)

for veggie in v:
    print(veggie)
