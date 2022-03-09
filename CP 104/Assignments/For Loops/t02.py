"""
-------------------------------------------------------
Assignment 5, Task 2
(Running on a treadmill burns a certain number of calories)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-07"
-------------------------------------------------------
"""
# Import
from functions import calories_burned

# Users input
per_minute = float(input("Calories burned per minute:"))
minutes = int(input("Total number of minutes ran:"))

# Display
calories_burned(per_minute, minutes)
