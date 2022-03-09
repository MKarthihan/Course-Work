"""
-------------------------------------------------------
Lab 5, Task 1
(Recursive function - example of tree recursion)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import recurse

# User input
x = int(input("Enter a Integer: "))
y = int(input("Enter another Integer: "))

# Call out
ans = recurse(x, y)

# Display
print(f"Answer: {ans}")

