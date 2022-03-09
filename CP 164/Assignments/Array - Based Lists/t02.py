"""
-------------------------------------------------------
Assignment 5, Task 2
(Sorted_List methods with Food objects)
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Import
from Sorted_List_array import Sorted_List

# Clean Method
lst = Sorted_List()
lst.insert(3)
lst.insert(6)
lst.insert(6)
lst.clean()

print("")
print("Edited: ")
for value in lst:
    print(value)

# Contains Method
print("")
print("Edited: ")
print(3 in lst)

# Count Method
lst.insert(3)
print("")
print("Edited: ")
print(lst.count(3))

# __getitem__
print("")
print("Edited: ")
print(lst[2])

# Index Method
print("")
print("Edited: ")
print(lst.index(3))

# Intersection Method
lst2 = Sorted_List()
lst2.insert(3)
lst.insert(30)

lst3 = Sorted_List()
lst3.intersection(lst, lst2)
print("")
print("Edited: ")
for value in lst3:
    print(value)

# Is_identical Method
print("")
print("Edited: ")
print(lst.is_identical(lst2))

# Max Method
print("")
print("Edited: ")
print(lst2.max())

# Min Method
print("")
print("Edited: ")
print(lst2.min())

# Peek Method
print("")
print("Edited: ")
print(lst.peek())

# Remove Method
lst2.remove(3)
print("")
print("Edited: ")
for value in lst2:
    print(value)

# Remove front Method
lst.remove_front()
print("")
print("Edited: ")
for value in lst1:
    print(value)

# Remove Many Method
lst4 = Sorted_List()
lst4.insert(1)
lst4.insert(2)
lst4.insert(2)
lst4.remove_many(2)
print("")
print("Edited: ")
for value in lst4:
    print(value)

# Split Method
lst4.insert(50)
lst4.insert(5)
target1, target2 = lst4.split()
print("")
print("Edited: ")
for value in target1:
    print(value)

# Split_alt Method
target1.method(50)
target2.method(500)
target3, target4 = target1.split_alt()
print("")
print("Edited: ")
for value in target3:
    print(value)
print("")
print("Edited: ")
for value in target4:
    print(value)

# Split_key Method
target3.insert(10)
target3.insert(100)
target5, target6 = target3.split_key(100)
print("")
print("Edited: ")
for value in target6:
    print(value)

# Union Method
target3.union(target5, target6)
print("")
print("Edited: ")
for value in target3:
    print(value)