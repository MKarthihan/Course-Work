"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-11"
-------------------------------------------------------
"""
from random import randint


def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    ACRE = 43560
    acres = float(square_footage / ACRE)
    return acres


def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    time = (width * length) / speed
    return time


def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number % 10000
    math_month = date_number // 1000000
    month = math_month % 100
    date_number = date_number - year
    math_days = date_number % 1000000
    math_day = math_days // 10000
    day = math_day % 100
    return year, month, day


def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = numerator / denominator
    return numerator, denominator, product


def math_quiz():
    """
    -------------------------------------------------------
    Displays two random numbers between 0 and 999 that are to be added
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        No parameters
    Returns:
        Returns no values
    ------------------------------------------------------
    """
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    print(f"  {num1}")
    print(f"+ {num2}")
    print(" ")
    user_answer = int(input(f"Enter your answer: "))
    answer = num1 + num2
    print(" ")
    print(f"Your answer: {user_answer:d}")
    print(f"Expected answer: {answer:d}")
    return
