"""
-------------------------------------------------------
Assignment 1, Task 1
(Removes all duplicate values from a list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import clean_list

# Users input
import random
 
values=[]
n = random.randint(10,20)
for i in range(n):
    values.append(random.randint(0,9))
# Call outs
print(f"Values: {values}")
clean_list(values)
