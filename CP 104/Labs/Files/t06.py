"""
-------------------------------------------------------
Lab 10, Task 6
(Statistics on the numbers)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# Import
from functions import number_stats

# User input
fh = open("numbers.txt", "r", encoding="utf-8")
# Call out
smallest, largest, total, average = number_stats(fh)

# Display
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
fh.close()
