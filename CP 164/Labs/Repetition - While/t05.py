"""
-------------------------------------------------------
Lab 7, Task 5
(Series of positive numbers, then calculates and returns
the minimum, maximum, total, and average of those numbers)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-04"
-------------------------------------------------------
"""
# IMPORT
from functions import positive_statistics

# Call out
minimum, maximum, total, average = positive_statistics()

# Display
print(" ")
print(f"minimum: {minimum:.2f}")
print(f"maximum: {maximum:.2f}")
print(f"total: {total:.2f}")
print(f"average: {average:.2f}")
