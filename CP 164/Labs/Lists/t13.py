"""
-------------------------------------------------------
Lab 8, Task 13
(List that is the union of the contents)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# Import
from functions import union

from random import randint

# List
source1 = [randint(-100, 100) for i in range(randint(1, 10))]
source2 = [randint(-100, 100) for i in range(randint(1, 10))]

# Call out
target = union(source1, source2)

# Display
print(f"Values 1: {source1}")
print(f"Values 2: {source2}")
print("")
print(f"Union: {target}")
