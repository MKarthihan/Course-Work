"""
-------------------------------------------------------
Lab 4, Task 5
(__getitem__ and __setitem__ methods)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
# Import
from List_array import List

# List
lst = List()
lst.append(0)
lst.append(3)
lst.append(6)
lst.append(-3)
lst.append(-6)

print(lst[3])
lst[0] = 69
print(lst[0])