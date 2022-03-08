"""
-------------------------------------------------------
Lab 10, Task 12
(First word with shortest length)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# Import
from functions import find_shortest

# User input
fh = open("words.txt", "r", encoding="utf-8")
print(f"file 'words.txt' open for reading")

# Call out
word = find_shortest(fh)

# Outputs
print(f"'{word}' is the first shortest word")
fh.close()
