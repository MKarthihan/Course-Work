"""
-------------------------------------------------------
Lab 7, Task 7
(The costs of breakfast, lunch, and supper for each day the user was away)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-03"
-------------------------------------------------------
"""
# import
from functions import meal_costs

# Call outs
b_total, l_total, s_total, a_total, = meal_costs()

# Display
print("Total:")
print(f"Breakfast:   ${b_total:.2f}")
print(f"Lunch:   ${l_total:.2f}")
print(f"Supper:   ${s_total:.2f}")
print(" ")
print(f"Grand total: ${a_total:.2f}")
