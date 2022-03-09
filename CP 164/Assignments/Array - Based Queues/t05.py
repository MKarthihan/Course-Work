"""
-------------------------------------------------------
Assignment 4, Task 5
(Splits a priority queue into two depending on an external priority key)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-02"
-------------------------------------------------------
"""
# Import
from Priority_Queue_array import Priority_Queue

# Queue
source = Priority_Queue()
source.insert(100)
source.insert(25)
source.insert(75)
source.insert(25)
source.insert(50)

key = 2

# Call out
target1, target2 = source.split_key(key)

# Display 
print("Target 1:")
while len(target1) > 0:
    print(target1.remove())

print("")

print("Target 2:")
while len(target2) > 0:
    print(target2.remove())