"""
-------------------------------------------------------
Lab 7, Task 3
(Number of years to reach a target population)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-04"
-------------------------------------------------------
"""
# Import
from functions import population_growth

# Users input
target = int(input("Target population:"))
current = int(input("Current population:"))
rate = int(input("Percent rate of growth:"))

# call outs
years = population_growth(target, current, rate)

# Display
print(
    f"It would take {years:d} years for a population of {current:d} to reach {target:d} from a rate of {rate:d}% growth ")
