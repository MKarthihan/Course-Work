"""
-------------------------------------------------------
Lab 4, Task 6
(array_to_list, list_to_array method )
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-05"
-------------------------------------------------------
"""
# Import
from List_array import List
from utilities import array_to_list, list_to_array

# List
llist = List()
source = [3,6,9,12,15]

array_to_list(llist, source)

print("List: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("List: ")
for value in source:
    print(value)