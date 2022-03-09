"""
-------------------------------------------------------
Lab 2, Task 5
(Total Pay)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""
# Users input of Rate of pay & Hours worked
rateofpay = float(input("Hourly rate of pay: $"))
hours_worked = float(input("Hours worked in the week: "))

# Calculate and display user input of Total pay
total_pay = rateofpay * hours_worked

print("")
print("Total pay for the week: $", total_pay)
