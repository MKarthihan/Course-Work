"""
-------------------------------------------------------
Assignment 8, Task 5
(Word chain)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""
# Import
from functions import is_word_chain

# User input
string = str(input("Enter words with a space in between them: "))
word_list = string.split(" ")

# Call outs
word_chain = is_word_chain(word_list)

# Display
if word_chain == True:
    print(f"{word_list} is a Word Chain")
elif word_chain == False:
    print(f"{word_list} is a Not a Word Chain")
