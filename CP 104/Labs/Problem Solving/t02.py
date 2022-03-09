"""
-------------------------------------------------------
Lab 2, Task 2
(Fahrenheit to Celsius)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""
# Constants
FREEZE = 32
# Users input of fahrenheit
fahrenheit = int(input("Enter the °F temperature to be converted in °C"))

# Calaculate and display user input into celsius
celsius = (fahrenheit - 32) * (5 / 9)

print("Temperature (F):", fahrenheit)
print("Temperature (C):", celsius)
