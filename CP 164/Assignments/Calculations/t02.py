"""
-------------------------------------------------------
Assignment 2,  Task 2
(Difference of the two digits)
-------------------------------------------------------
Author:  Karthihan Maheswaram
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-30"
-------------------------------------------------------
"""
# Users Input
numbers = int(input("Enter a positive digit number:"))

# Constant
difference = 0

# Calculate the difference of the two digits
number_one = numbers // 10
number_two = numbers % 10
difference = difference + number_two
final = (number_one - number_two)

# Display the difference of the two digits
print(f"The difference of the digits of {numbers:d} is {final:d}")
