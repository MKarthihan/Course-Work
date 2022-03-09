"""
-------------------------------------------------------
Assignment 4, Task 1
(Corresponding day of the week)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Import
from functions import day_of_week

# Users Input
day_number = int(input("Enter a number between 1 to 7:"))

# Call outs from import
result = day_of_week(day_number)

# Display
if 1 <= day_number <= 7:
    print(f"{day_number:d} is corresponding to {result:s} of the week ")
elif 1 > day_number or day_number > 7:
    print(f"{day_number:d} is a {result:s}...Try again!")
