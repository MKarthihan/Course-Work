"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Karthihan Maheswaran
__updated__ = "2021-09-26"
-------------------------------------------------------
"""
# Users input on interest, compounded years. principal, & years
interest = float(input("Annual rate of interest (as a decimal):"))
compounded = int(input("Number of times the interest is compounded per year:"))
principal = float(input("Initial amount of dollars?:"))
years = int(input("How long did you have or plan to have this loan?:"))

# Calculate the compound interest with give in user inputs
bracket = (1 + (interest / compounded))
expo = compounded * years
stepo = bracket ** expo
final = principal * stepo

# Display Principal, Interest, Number of years, compounded years, & balance
print("")
print("Principal: $", principal)
print("Interest:", interest * 100, "%")
print("Number of years:", years)
print("Number of times interest compounded per year:", compounded)
print("""
Balance: $""", round(final, 2))
