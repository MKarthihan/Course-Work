"""
-------------------------------------------------------
Assignment 3, Task 4
(Reverses the contents of the source stack)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Import
from Stack_array import Stack
from utilities import array_to_stack
from t01 import values

# Stack Formation 
source = Stack()

array_to_stack(source, values)

source.reverse()

# Display
while not source.is_empty():
    ele = source.pop()
    print(ele)