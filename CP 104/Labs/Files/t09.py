"""
-------------------------------------------------------
Lab 10, Task 9
(Number of appearances of value)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# Import
from functions import count_frequency_value

# User input
fh = open("numbers.txt", "r")
number = fh.read()
print(f"file 'numbers.txt' open for reading")
value = str(input("Value to count:"))

# Call out
count = count_frequency_value(fh, value)


# Outputs
print(f"{value} appears {count} time(s)")
fh.close()
