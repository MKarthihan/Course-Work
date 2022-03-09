"""
-------------------------------------------------------
Lab 3, Task 4
(Discount)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-28"
-------------------------------------------------------
"""
# Users input for number & percent
number = float(input("Enter number:"))
percent = float(input("Enter percent:"))

# Calculate the discount value
discount = number * (percent / 100)

# Display the percent Discount, Number, and the Discount
print(f"A {percent:.1f} percent discount on {number:.1f} is {discount:.2f}")
