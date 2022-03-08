"""
-------------------------------------------------------
Lab 7, Task 1
(Plays a random higher-lower guessing game)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-04"
-------------------------------------------------------
"""
# Import
from functions import hi_lo_game

# Users input
high = int(input("Enter the max value for the range (0 - value):"))

# call outs
count = hi_lo_game(high)

# Display
print(f"You made {count:d} guesses.")
