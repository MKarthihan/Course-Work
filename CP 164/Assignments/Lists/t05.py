"""
-------------------------------------------------------
Assignment 7, Task 5
(Whether a list is sorted)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-17"
-------------------------------------------------------
"""
# Import
from functions import is_sorted

# Users input - List
values = []
value = int(input("Enter number of elements : "))
for i in range(0, value):
    count = 0
    count = count + i
    elements = int(input(f"Index {count}:"))
    values.append(elements)
print(values)

# Call out
in_order, index = is_sorted(values)

# Display
print(f"{in_order}, {index}")
