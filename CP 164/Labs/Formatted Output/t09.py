"""
-------------------------------------------------------
Lab 3, Task 9
(Clothes)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-30"
-------------------------------------------------------
"""
# User inputs for cost of products
sweat_band = float(input("Enter sweatband cost: $"))
pants = float(input("Enter pants cost: $"))
jacket = float(input("Enter jacket cost: $"))

# Calculate the total cost of all the products
total_cost = float(sweat_band + pants + jacket)

# Display the Prices and the total value
print(f"Clothing     Cost")
print(f"Sweatband    ${sweat_band:6.2f}")
print(f"Pants        ${pants:6.2f}")
print(f"Jacket       ${jacket:6.2f}")
print(f"Total        ${total_cost:6.2f}")
