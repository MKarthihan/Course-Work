"""
-------------------------------------------------------
Assignment 2,  Task 4
(Birthday Party Balloons)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-01"
-------------------------------------------------------
"""
# Users input for balloons and children
balloons = int(input("Number of balloons:"))
children = int(input("Number of children:"))

# Calculate the ratio balloons and balloon left
balloon_ratio = (balloons // children)
balloon_left = (balloons % children)

# Display the given out balloons with balloons not given out
print(f"Each child receives {balloon_ratio} balloons")
print(f"Balloons that won’t be distributed: {balloon_left}")
