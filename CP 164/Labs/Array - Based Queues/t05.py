"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Import
from Priority_Queue_array import Priority_Queue

# User input
value = int(input("Value: "))

# Queue
pq = Priority_Queue()
pq.insert(value)

# Display
print(pq.remove())