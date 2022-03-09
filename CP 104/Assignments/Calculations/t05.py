"""
-------------------------------------------------------
Assignment 2,  Task 5
(Building a simple shed)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
# Users input of dimensions and cost of materials
foundation_lenth = float(input("Foundation length (m):"))
foundation_width = float(input("Foundation width (m):"))
foundation_height = float(input("Foundation height (m):"))
wall_height = float(input("Wall height (m):"))
cost_concrete = float(input("Cost of concrete ($/m^3):"))
cost_bricks = float(input("Cost of bricks (s/m^2):"))

# Calculate needed materials with the total price of it
concrete_needed = foundation_lenth * foundation_width * foundation_height
totalcost_concrete = cost_concrete * concrete_needed
bricks_needed = ((foundation_width * wall_height) * 2) + \
    ((foundation_lenth * wall_height) * 2)
totalcost_bricks = cost_bricks * bricks_needed
totalcost = totalcost_concrete + totalcost_bricks

# Display the needed materials with the total cost of everything
print("")
print(f"Concrete needed for foundation (m^3): {concrete_needed:.2f}")
print(f"Cost of concrete: ${totalcost_concrete:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed:.2f}")
print(f"Cost of bricks: ${totalcost_bricks:,.2f}")
print(f"Total cost: ${totalcost:,.2f}")
