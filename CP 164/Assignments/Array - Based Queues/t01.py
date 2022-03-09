"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-02"
-------------------------------------------------------
"""
# Import
from Queue_circular import Queue

# Queue
queue = Queue(2)

# Display
print(len(queue))
print(queue.is_empty())

queue.insert(25)
print(len(queue))

values = queue.peek()
print(values)

out = queue.remove()
print(out)

queue.insert(25)
queue.insert(50)
print(queue.is_full())