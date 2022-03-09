"""
-------------------------------------------------------
Lab 3, Task 6
(Tests priority queue implementation)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Import
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
from Food_utilities import read_foods

# File opening 
file_variable = open("foods.txt", "r")

foods = read_foods(file_variable)

# List
source = [1,2,3,4,5] 

# Queue
pq = Priority_Queue()

while len(pq) > 0:
    value = pq.remove()
    print(value)
    source.append(value)

array_to_pq(pq, source)
pq_to_array(pq, source)

print(source)

file_variable.close()

priority_queue_test(foods)