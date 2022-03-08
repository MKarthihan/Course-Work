# --------------------------------
# Module 1 –Introduction to Python
# Case Study
# --------------------------------

# PSA: While running the code, run part 1 and 2 separately by commenting each part .

# Part 1
# Import Lake Ontario Swimmers data
import csv
swim = open('LakeOntarioSwimmers-csv-format-cleaned.csv')
csv_Swim = csv.reader(swim)

for row in csv_Swim:
    print(row)

swim.close()

# Part 2
# Deaths and age-specific mortality rates, by selected grouped causes
# Link: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1310039201
import csv
death = open('1310039201-eng.csv')
csv_Death = csv.reader(death)

for row in csv_Death:
    print(row)

death.close()



