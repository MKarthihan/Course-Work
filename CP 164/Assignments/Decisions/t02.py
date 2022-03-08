"""
-------------------------------------------------------
Assignment 4, Task 2
(Pollution level)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""
# Import
from functions import pollution_level

# Users input
aqi = int(input("Enter the AQI (Air Quality Index):"))

# Call out from Import
level = pollution_level(aqi)

# Display
print(f"Pollution level {aqi:d}: {level:s}")
