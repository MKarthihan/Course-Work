"""
-------------------------------------------------------
Lab 4, Task 4
(index, find, __contains__, count, max, and min methods)
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

print(lst.index(-3))

print(lst.find(-3))

if 6 in lst:
    print("6 is in the list")
else:
    print("6 not in the list")
    
print(lst.count(0))
print(lst.min())
print(lst.max())