"""
-------------------------------------------------------
Assignment 2,  Task 1
(Projected Tax Report)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-30"
-------------------------------------------------------
"""
# Constant
TAX = 22.50

# User input  for total sale value
total = float(input("Enter the total sales: $"))

# Calculate the total tax
total_tax = total * (TAX / 100)

# Display the Projected Tax Report
print(f"Projected Tax Report")
print(f"--------------------------")
print(f"Total sales:   ${total:.2f}")
print(f"Annual tax:    %{TAX:.2f}")
print(f"--------------------------")
print(f"Tax:           ${total_tax:.2f}")
