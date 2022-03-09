"""
-------------------------------------------------------
Lab 8, Task 7
(Categories of values in a list)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-12"
-------------------------------------------------------
"""
# Import
from functions import list_categorize
from random import randint

# Lists
values = [randint(-100, 100) for i in range(randint(1, 10))]

# Call out
negatives, positives, zeroes, evens, odds = list_categorize(values)

# Display
print(f"Values: {values}")
print(" ")
print(f"Negatives: {negatives}")
print(f"Positives: {positives}")
print(f"Zeroes: {zeroes}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")
