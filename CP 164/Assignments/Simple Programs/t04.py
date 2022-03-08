"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Karthihan Maheswaran
__updated__ = "2021-09-26"
-------------------------------------------------------
"""
# Users input of the cost of 1 burrito & how many burritos they want
amount = float(input("Cost of 1 burrito: $"))
burrito = int(input("How many burritos do you want?"))

# Calculate the total price of how many the burrtios the user wants
total = burrito * amount

# Round to the closest two decimal place
dollars = (round(total, 2))

# Display the total cost and how many burritos
print("Total cost of", burrito, "burritos: $", dollars)
