"""
-------------------------------------------------------
Lab 2, Task 5
(Tests the methods of Stack for empty and non-empty stacks using the data in source)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
#Imports
from utilities import stack_test
from Food_utilities import read_foods

# File opening
file = open("foods.txt", 'r')
source = read_foods(file)
file.close()

# Call out / Display
print(stack_test(source))
