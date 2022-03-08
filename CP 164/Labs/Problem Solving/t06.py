"""
-------------------------------------------------------
Lab 2, Task 6
(Mortgage Payment)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""
# Users inputs
principal = float(input("Mortgage principal: $"))
years = int(input("Number of years: "))
interest = float(input("Yearly interest rate (%): "))

# Calculate the total amount of months in a year
monthly = years * 12

# Calculate the total monthly interest rate
monthly_rate = ((interest / 100) / 12)

# Calculate the numerator of the formula with the users input
numerator = (monthly_rate * ((1 + monthly_rate)**monthly))

# Calculate the numerator of the formula with the users input
denominator = ((1 + monthly_rate)**monthly) - 1

# Calculate the total monthly payments
operation = (principal * (numerator / denominator))

# Rounding the values to two decimal places
operation = str(round(operation, 2))

# Display the total monthly payments
print("The monthly payments are: $", operation)
