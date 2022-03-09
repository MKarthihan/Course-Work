"""
-------------------------------------------------------
Lab 6, Task 15
(Statistics)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""
# Import
from functions import statistics

# Users input
n = int(input("Enter number of values:"))

# Call outs
minimum, maximum, total, average = statistics(n)

# Call out
print(" ")
print("Minimum: {:.2f}".format(minimum))
print("Maximum: {:.2f}".format(maximum))
print("Total: {:.2f}".format(total))
print("Average: {:.2f}".format(average))
