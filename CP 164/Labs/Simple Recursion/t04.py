"""
-------------------------------------------------------
Lab 5, Task 4
(Calculates base^power.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-15"
-------------------------------------------------------
"""
# Import 
from functions import to_power

# User input
base = float(input("Enter a Float base: "))
power = int(input("Enter another power Integer: "))

# Call out
ans = to_power(base, power)

# Display
print(f"Answer: {ans}")