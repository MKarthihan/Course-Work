"""
-------------------------------------------------------
Assignment 3, Task 2
(Mow lawn speed)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-11"
-------------------------------------------------------
"""
# Import
from functions import mow_lawn

# Users input
width = float(input("Width (m):"))
length = float(input("Length (m):"))
speed = float(input("Speed (m^2/minute):"))

# Call outs from import
time = mow_lawn(width, length, speed)

# Display the time required
print(f"Mowing the law takes {time:.2f} minutes")
