"""
-------------------------------------------------------
Lab 10, Task 2
(Record for a given ID in a sequential file)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-25"
-------------------------------------------------------
"""
# Import
from functions import customer_by_id

# User input
fh = open("customers.txt", "r", encoding="utf-8")
print(f"Find customer by id_number")
id_number = str(input("Enter an ID: "))

# Call out
result = customer_by_id(fh, id_number)

# Outputs
print(f"{result}")
fh.close()
