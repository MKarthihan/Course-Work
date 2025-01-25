#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Testing Code File
#  CP 321 A1
#  testing.py
#  Karthihan Maheswaran
#  01/26/2025
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
from functions import modifier, grade_stats, matrix_manipulator

# Test for modifier
print("="*50)
data = np.array([[1, 2, 3], [2, 3, 4], [5, 6, 7]])
print("Testing modifier:")
means = modifier(data)
print("\n" + "="*50 + "\n")

# Test for grade_stats
grades = np.array([[123456, 9, 8, 0, 2], [234567, 8, 8, 0, 5],[345678, 9, 8, 6, 10], [456789, 8, 7, 7, 10]])
print("Testing grade_stats:")
grade_stats(grades)
print("\n" + "="*50 + "\n")

# Test for matrix_manipulator
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Testing matrix_manipulator:")
matrix_manipulator(A, B)
print("="*50)
