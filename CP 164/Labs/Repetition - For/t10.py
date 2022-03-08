"""
-------------------------------------------------------
Lab 6, Task 10
(Calories burnt on a treadmill)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-25"
-------------------------------------------------------
"""
# Import
from functions import treadmill

# Users input
burnt_per_minute = float(input("Enter calories burned per minute:"))
start = int(input("Enter beginning number of minutes:"))
end = int(input("Enter ending number of minutes:"))
inc = int(input("Enter the increment in minutes:"))

# Display
print(" ")
treadmill(burnt_per_minute, start, end, inc)
