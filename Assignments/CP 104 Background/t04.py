"""
-------------------------------------------------------
Assignment 1, Task 4 
(Leap year determination)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
# Import
from functions import is_leap_year

# Users input
year = int(input("Enter a year: "))

# Call out
leap_year = is_leap_year(year)

# Display
print(f"Is {year} a leap year?... it is {leap_year}!")