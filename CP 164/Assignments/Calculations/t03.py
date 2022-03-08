"""
-------------------------------------------------------
Assignment 2,  Task 3
(Date in the format)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
# Users input for date
date = int(input("Enter a date in the format MMDDYYYY:"))

# Calculate to separate given date
month = date // 1000000
year = date % 10000
date = date - year
day = date % 1000000
final_day = day // 10000

# Display reformatted date
print(f"The reformatted date: {year}/{month}/{final_day}")
