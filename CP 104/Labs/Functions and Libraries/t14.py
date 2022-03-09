"""
-------------------------------------------------------
Lab 4, Task 14
(seconds is the same as...)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-08"
-------------------------------------------------------
"""
# Import
from functions import time_values

# User input
seconds = int(input("Number of seconds:"))

# Call out from import
days = time_values(seconds)
hours = time_values(seconds)
minutes = time_values(seconds)

# Display
print(f"""{seconds:d} seconds is the same as:
  {days[0]:d} days
  {hours[1]:d} hours
  {minutes[2]:d} minutes""")
