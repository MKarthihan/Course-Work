"""
-------------------------------------------------------
Lab 5, Task 6
(Copies elements of a bag to a set.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import bag_to_set

# User input
bag = [11, 44, 22, 55, 33, 11, 44, 22, 55, 33, 11, 44, 22, 55, 33]

# Call out
new_set = bag_to_set(bag)

# Display
print(f"Old List: {bag}")
print(f"New List: {new_set}")