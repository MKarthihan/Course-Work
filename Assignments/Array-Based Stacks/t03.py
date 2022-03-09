"""
-------------------------------------------------------
Assignment 3, Task 3
(Reverses the contents of a stack)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Import
from Stack_array import Stack
from functions import stack_reverse
from utilities import array_to_stack
from t01 import values

# Stack Formation
source = Stack()

array_to_stack(source, values)

#Call out
stack_reverse(source)

# Display
while not source.is_empty():
    ele = source.pop()
    print(ele)
    