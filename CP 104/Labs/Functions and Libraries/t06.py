"""
-------------------------------------------------------
Lab 4, Task 6
(Circle Defined by a Right Triangle)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-07"
-------------------------------------------------------
"""
# Import
from functions import pythag

# Users Input
s1 = float(input("Length of side 1:"))
s2 = float(input("Length of side 2:"))

# Call out from import
radius = pythag(s1, s2)
diam = pythag(s1, s2)
circ = pythag(s1, s2)
area = pythag(s1, s2)

# Display the calculated Radius, Diameter, Circumference, Area
print(f"Radius of resulting circle: {radius[0]:.2f}")
print(f"Diameter of resulting circle: {diam[1]:.2f}")
print(f"Circumference of resulting circle: {circ[2]:.2f}")
print(f"Area of resulting circle: {area[3]:.2f}")
