"""
-------------------------------------------------------
Lab 3, Task 3
(Tests queue implementation)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-29"
-------------------------------------------------------
"""
# Import
from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test

# List
source = [54,64,564,184,25]

# Queue
queue = Queue()
array_to_queue(queue, source)

for leng in range(len(queue)):
    value = queue.remove()
    print(value)
    source.append(value)

queue_to_array(queue, source)

print(source)

queue_test(source)