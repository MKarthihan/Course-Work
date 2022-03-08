"""
-------------------------------------------------------
Lab 6, Task 6
(Prints a triangle using a character)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
# Import
from functions import draw_triangle

# Users input
height = int(input("Enter the height in characters:"))
char = str(input("Enter the draw character:"))

# Display
draw_triangle(height, char)
