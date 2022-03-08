"""
-------------------------------------------------------
Lab 9, Task 2
(URL represents a business, a non-profit, or
 another type of organization.)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""
# Import
from functions import url_categorize

# Users input
url = str(input("Enter the website address:"))

# Call out
url_type = url_categorize(url)

# Display
print(f"{url_type:s}")
