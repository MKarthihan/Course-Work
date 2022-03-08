"""
-------------------------------------------------------
Assignment 4, Task 4
(Secondary colour from mixing two primary)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Import
from functions import rgb_mix

# Users input
rgb1 = str(input("Enter colour 1 (red, green, blue):"))
rgb2 = str(input("Enter colour 2 (red, green, blue):"))

# Call outs from Import
colour = rgb_mix(rgb1, rgb2)

# Display
print(f"{rgb1:s} + {rgb2:s} = {colour:s}")
