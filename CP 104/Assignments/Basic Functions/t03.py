"""
-------------------------------------------------------
Assignment 3, Task 3
(Reformatted date)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-11"
-------------------------------------------------------
"""
# Import
from functions import date_extract

# Users input
date_number = int(input("Enter a date in the format MMDDYYYY:"))

# Call outs from import
year = date_extract(date_number)
month = date_extract(date_number)
day = date_extract(date_number)

# Display reformatted date
print(f"The reformatted date: {year[0]:d}/{month[1]:02d}/{day[2]:02d}")
