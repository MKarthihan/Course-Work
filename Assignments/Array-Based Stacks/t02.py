"""
-------------------------------------------------------
Assignment 3, Task 2
(Combines two source stacks into the current target stack.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack
from t01 import values, values_2

# Stack Formation
source1 = Stack()
source2 = Stack()

array_to_stack(source1, values)
array_to_stack(source2, values_2)

# Call out
target = Stack()
target.combine(source1, source2)

# Display
while not target.is_empty():
    ele = target.pop()
    print(ele)
