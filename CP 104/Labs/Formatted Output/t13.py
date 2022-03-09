"""
-------------------------------------------------------
Lab 3, Task 13
(Seconds Calculations)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-28"
-------------------------------------------------------
"""
# Users input for total seconds
seconds = int(input("Enter number of seconds:"))

# Constants
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Calculate the seconds in each category
total = seconds // 1
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds_left = seconds % 60

# Display the hours, minutes and the seconds left from the total seconds
print(
    f"There are {hours} hours, {minutes} minutes, and {seconds_left} seconds in {total} seconds")
