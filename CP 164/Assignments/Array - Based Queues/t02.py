"""
-------------------------------------------------------
Assignment 4, Task 2
(Splits the source queue into separate target queues with values)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-02"
-------------------------------------------------------
"""
# Import
from Queue_circular import Queue
from functions import queue_split_alt

# Queue
source = Queue(2)
source.insert(1)
source.insert(2)

# Call out
target1, target2 = queue_split_alt(source)

# Display
print("Target 1:")
while len(target1) > 0:
    print(target1.remove())
print("")
print("Target 2:")
while len(target2) > 0:
    print(target2.remove())