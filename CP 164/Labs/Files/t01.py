"""
-------------------------------------------------------
Lab 10, Task 1
(n-th record in a comma-delimited sequential file)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-25"
-------------------------------------------------------
"""
# Import
from functions import customer_record

# User input
fh = open("customers.txt", "r", encoding="utf-8")
print(f"Find record n")
n = int(input("Enter a record number: "))

# Call out
result = customer_record(fh, n)

# Outputs
print(f"{result}")
fh.close()
