"""
-------------------------------------------------------
Lab 5, Task 5
(Leap year)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Import
from functions import is_leap
# User input
year = int(input("Enter a year (>0):"))

# Call out from import
result = is_leap(year)

# Display
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print(f"{year:d} is a leap year")
else:
    print(f"{year:d} is not a leap year")
