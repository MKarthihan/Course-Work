"""
-------------------------------------------------------
Lab 2, Task 12
(Seconds Conversion)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-09-24"
-------------------------------------------------------
"""
# Users input of number of seconds
seconds = int(input("Number of seconds:"))

# Conversion of Seconds to day
SECONDS_PER_DAY = 86400

# Conversion of Seconds to hour
SECONDS_PER_HOUR = 3600

# Conversion of Seconds to minute
SECONDS_PER_MINUTE = 60

# Calculate for days with seconds with the users input
day = seconds // 86400

# Calculate for remaining seconds with operation before
seconds = seconds % 86400

# Calculate for hours with seconds with the users input
hours = seconds // 3600

# Calculate for remaining seconds with operation before
seconds = seconds % 3600

# Calculate for minutes with seconds with the users input
minutes = seconds // 60

# Calculate for remaining seconds with operation before
seconds = seconds % 60
seconds_left = seconds

# Display the amount of Days, Hours, Minutes, and Seconds are from Users input.
print("Days:", day, "Hours:", hours, "Minutes:",
      minutes, "Seconds:", seconds_left)
