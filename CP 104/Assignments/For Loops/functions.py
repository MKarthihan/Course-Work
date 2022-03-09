"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-07"
-------------------------------------------------------
"""


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(2, num + 1, 1):
        product *= i
    return product


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Prints calories burned every five minutes given the
    number of calories burned per minute an the total number
    of minutes run.
    Use = calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
       per_minute - calories burned per minute (float > 0)
       minutes - total number of minutes ran (float > 0)
    Returns:
        N/A
    ------------------------------------------------------
    """
    for x in range(5, minutes + 1, 5):
        calories_total = per_minute * x
        print(f"{x:3d}:{calories_total:6.1f}")
    return


def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Prints a triangle of # characters with an empty center
    Use: result = open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of lines (int > 0)
    Returns:
        N/A
    ------------------------------------------------------
    """
    char = "#"
    for i in range(1, num_rows + 1):
        print(f"{char:{' '}<{i}}{char}")
    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("       ", end="")
    for i in range(start, stop + 1):
        print(f"{i:4d}", end="")
    print("")
    print("       " + "----" * (stop + 1 - start))
    for i in range(start, stop + 1):
        print("")
        print(f"{i:>5d} |", end="")
        for j in range(start, stop + 1):
            product = i * j
            print(f"{product:4d}", end="")
    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    end = start + (count * increment)
    for x in range(start, end, increment):
        total += x
    return total
