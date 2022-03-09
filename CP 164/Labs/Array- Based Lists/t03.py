"""
-------------------------------------------------------
Lab 4, Task 3
(insert, append, and remove methods)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-31"
-------------------------------------------------------
"""
# Import
from List_array import List

# List/Display
lst = List()
lst.append(50)
print(len(lst))

lst.insert(0, 100)
print(len(lst))

remove = lst.remove(50)

print(remove)