"""
-------------------------------------------------------
Assignment 5, Task 1
(List methods with Food objects)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Import
from Food import Food
from Food_utilities import read_food, read_foods
from List_array import List
from utilities import array_to_list

# File
file = open("foods.txt", "rt")
foods = read_foods(file)
file.close()

# List 1
lst = List()
array_to_list(lst, foods)

# Append Method
lobster = Food("Lobster Tail", 0, False, 500)
lst.append(lobster)
print("Edited: ")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")

# Clean Method
lst.clean()

print("")
print("Edited:  ")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")

# Combine Method
temp_lst = [read_food("Onion Soup|0|True|250"), read_food("Pork Belly|1|False|350")]

# List 2
lst2 = List()
lst2.append(temp_lst[0])
lst2.append(temp_lst[1])

# List 3
lst3 = List()
lst3.combine(lst, lst2)
print("")
print("Edited: ")
for value in lst3:
    print(f"{value.name}")

# __getitem__
print("")
print("Edited :")
print(lst3[10])

# Intersection Method
lst2.append(temp_lst[0])
lst2.append(temp_lst[1])

# List 4
lst4 = List()
lst4.intersection(lst2, lst3)
print("")
print("Edited: ")
for value in lst4:
    print(f"{value.name}")

# Is_identical Method
print("")
print("Edited: ")
print(lst4.is_identical(lst2))

# Prepend Method
lst4.prepend(temp_lst[0])
print("")
print("Edited: ")
for value in lst4:
    print(f"{value.name}")

# Remove Front Method
lst4.remove_front()
print("")
print("Edited: ")
for value in lst4:
    print(f"{value.name}")

# Remove many Method
lst4.append(temp_lst[0])
lst4.remove_many(temp_lst[0])
print("")
print("Edited: ")
for value in lst4:
    print(f"{value.name}")
    
# Split Method
target1, target2 = lst3.split()

print("")
print("Edited: ")
for value in target1:
    print(f"{value.name}")

print("")
print("Edited: ")
for value in target2:
    print(f"{value.name}")

# Split Alt Method
target3, target4 = target1.split_alt()

print("")
print("Edited: ")
for value in target3:
    print(f"{value.name}")

print("")
print("Edited: ")
for value in target4:
    print(f"{value.name}")

# Union Method
lst3.union(target3, target4)
print("")
print("Edited: ")
for value in lst3:
    print(f"{value.name}")
    




    


