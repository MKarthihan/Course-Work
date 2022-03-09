"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Import
from Queue_array import Queue

# User input
value = input("Value: ")

# Queue 
queue = Queue()

queue.insert(value)

print("")
print(queue.peek())

values = queue.remove()

# Display
print("")
print(values)
