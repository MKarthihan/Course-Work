"""
-------------------------------------------------------
Assignment 6, Task 3
(Monthly interest and payments on a loan)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-14"
-------------------------------------------------------
"""
# Import
from functions import interest_table

# User input
principal = float(input("Principal:"))
rate = float(input("Interest rate:"))
payment = float(input("Monthly payment:"))

# Call out
interest_table(principal, rate, payment)
