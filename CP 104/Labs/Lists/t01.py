"""
-------------------------------------------------------
Lab 8, Task 1
(Name of a day of the week)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# Import

from functions import get_weekday_name
# User Input

d = int(input("Please enter a day: "))
# Call out

name = get_weekday_name(d)
# Display

print(name)
