"""
-------------------------------------------------------
Lab 9, Task 10
(Analyzes text)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import text_analyze

# User input
txt = str(input("Enter a string:"))

# Call out
uppr, lowr, dgts, whtspc = text_analyze(txt)

# Display
print(f"upper case letters: {uppr:d}")
print(f"lower case letters: {lowr:d}")
print(f"digits: {dgts:d}")
print(f"whitespace characters: {whtspc:d}")
