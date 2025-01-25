#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Function Code File
#  CP 321 A1
#  functions.py
#  Karthihan Maheswaran
#  01/26/2025
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np

def modifier(data):
    """
    Modifies the input 2D array and performs multiple operations.
    Parameters:
        data: A 2D numpy array.
    Returns:
        list: A list containing the column-wise means of the modified array.
    """
    print("If the data is:")
    print(data)

    first_row = data[0]
    last_row = data[-1]
    item1_output = f"{first_row[0]}, {first_row[-1]}, {last_row[0]}, {last_row[-1]}"
    print("\nOutput of item 1 above is:")
    print(item1_output)

    random_col = np.array([43, 24, 23]).reshape(-1, 1)
    data = np.hstack((data, random_col))
    print("\nOutput of item 2 above is:")
    print(data)

    second_last_row_reversed = data[-2][::-1]
    print("\nOutput of item 3 above is:")
    print(second_last_row_reversed)

    column_means = np.mean(data, axis=0).round(2).tolist()
    print("\nOutput of item 4 above is:")
    print(column_means)

    return column_means


def grade_stats(data):
    """
    Analyzes quiz scores in a 2D array and prints relevant statistics.
    The first column represents student IDs, and the subsequent columns represent quiz scores.
    Parameters:
        data : A 2D numpy array where the first column is student IDs and the other columns are quiz scores.
    Returns:
        None
    """
    print("If the ‘data’ is:")
    print(data)

    quiz_means = np.mean(data[:, 1:], axis=0)
    quizzes_above_70 = [f"Quiz {i + 1}" for i, mean in enumerate(quiz_means) if mean > 7]
    print("\nThe output for item 1 above is:")
    print("Quizzes with mean above 70%:", ", ".join(quizzes_above_70))

    student_means = np.mean(data[:, 1:], axis=1)
    students_above_79 = [int(data[i, 0]) for i, mean in enumerate(student_means) if mean > 7.9]
    print("\nThe output for item 2 above is:")
    print("Students with mean above 79%:", ", ".join(map(str, students_above_79)))

    students_full_score = [int(data[i, 0]) for i in range(data.shape[0]) if data[i, -1] == 10]
    print("\nThe output for item 3 above is:")
    print("Students with 100% in last quiz:", ", ".join(map(str, students_full_score)))


def matrix_manipulator(A, B):
    """
    Performs matrix operations on two square matrices, A and B.
    Parameters:
        A: A 2D square numpy array (matrix).
        B: A 2D square numpy array (matrix) of the same shape as A.
    Returns:
        None
    """
    print("If the ‘data’ is:")
    print("A =", A)
    print("B =", B)

    A_transpose = np.transpose(A)
    print("\nThe output for item 1 above is:")
    print(A_transpose)

    AB_dot = np.dot(A, B)
    print("\nThe output for item 2 above is:")
    print(AB_dot)

    result = AB_dot + np.transpose(B)
    print("\nThe output for item 3 above is:")
    print(result)
