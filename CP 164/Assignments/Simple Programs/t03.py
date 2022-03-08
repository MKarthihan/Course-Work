"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  Karthihan Maheswaran
__updated__ = "2021-09-26"
-------------------------------------------------------
"""
# Constant
CONVERSION = 1.609

# Users input on how many miles they desire
miles = float(input("Please enter your length in miles"))

# Calculate and Display miles to kilometres
kilometre = miles * CONVERSION
print("Length in miles:", miles)
print("Length in km:", kilometre)
