"""
-------------------------------------------------------
Assignment 7, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-17"
-------------------------------------------------------
"""


def list_factors(num):
    """
    -------------------------------------------------------
    List of the factors that make up that number
    excepting the number itself.
    Use: factor_list = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - A number of which the factors for would be found
    Returns:
        factor_list - A list of factors of num (list of int)
    ------------------------------------------------------
    """
    factor_list = []
    for factors in range(1, num - 1):
        if num % factors == 0:
            factor_list.append(factors)
    return factor_list


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    num = int(input("Enter a postive number:"))
    if num > 0:
        numbers.append(num)
    while num != 0:
        num = int(input("Enter a postive number:"))
        if num < 0:
            continue
        if num > 0:
            numbers.append(num)
    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    location = [first_element for first_element,
                element in enumerate(values) if element == target]
    return location


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    l3 = [x for x in minuend if x not in subtrahend]
    minuend.clear()
    minuend.extend(l3)
    return


def is_sorted(values):
    """
    -------------------------------------------------------
    Returns the sum of the even numbers in values.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    start = []
    start.extend(values)
    values.sort()
    if values == start:
        in_order = True
        index = -1
    elif values != start:
        in_order = False
        index = 1
    return in_order, index
