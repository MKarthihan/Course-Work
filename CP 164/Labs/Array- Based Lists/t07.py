"""
-------------------------------------------------------
Lab 4, Task 7
(Tests List implementation.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
# Import
from Food_utilities import read_foods
from utilities import list_test


# File opening
file = open("foods.txt", "rt")
source = read_foods(file)
file.close

list_test(source)