"""
-------------------------------------------------------
Lab 2, Task 8
(BMI calculation)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""
# User input of height
height = float(input("Enter your height (m):"))

# User input of weight
weight = float(input("Enter your weight(kg):"))

# User input of upper limit
limit = int(input("Enter your upper limit BMI 25 or 23):"))

# Calculate the height squared with the users input
height_square = float(height**2)

# Calculate the BMI of the formula with the users input
bmi = float(weight / height_square)

# Rounding the values to two decimal places
bmi = round(bmi, 2)

# Calculate the BMI Prime of the formula with the users input
bmi_prime = float(bmi / limit)

# Rounding the values to two decimal places
bmi_prime = round(bmi_prime, 2)

# Display the BMI & the BMI prime
print("Body Mass Index (kg/m^2) =", bmi)
print("BMI Prime =", bmi_prime)
