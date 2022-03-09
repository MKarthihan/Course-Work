"""
-------------------------------------------------------
Assignment 3, Task 1
(Combines two source stacks into a target stack)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
# Import 
from Stack_array import Stack
from functions import stack_combine
from utilities import array_to_stack
import random

# Stack Formation 
source1 = Stack()
source2 = Stack()

values=[]
n = random.randint(0,10)
for i in range(n):
    values.append(random.randint(0,5))
    
values_2=[]
n_2 = random.randint(0,10)
for i in range(n_2):
    values.append(random.randint(0,5))
    
array_to_stack(source1, values) 
array_to_stack(source1, values_2)

# Call out
target = stack_combine(source1, source2)

# Display
while not target.is_empty():
    ele = target.pop()
    print(ele)

