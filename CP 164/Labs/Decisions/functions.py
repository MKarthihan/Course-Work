"""
-------------------------------------------------------
Lab 5, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    result_v1 = target - v1
    result_v1 = abs(result_v1)
    result_v2 = target - v2
    result_v2 = abs(result_v2)
    if result_v1 > result_v2:
        result = v2
    else:
        result = v1
    return result


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        result = True
    else:
        result = False
    return result


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - description of earthquake damage (str)
    -------------------------------------------------------
    """
    if (5 <= intensity < 5.5):
        result = "Some damage"
    elif (5.5 <= intensity < 6.5):
        result = "Serious damage: walls may crack or fall"
    elif (6.5 <= intensity < 7.5):
        result = "Disaster: buildings may collapse"
    elif (intensity >= 7.5):
        result = "Catastrophe: most buildings destroyed"
    else:
        result = "Little or no damage"
    return result


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    MIN_EMPLOYED = 5
    MIN_ANNUAL = 30000
    year = int(input("Years employed:"))
    if year >= MIN_EMPLOYED:
        qualified = True
        salary = int(input("Annual salary:"))
        if salary >= MIN_ANNUAL:
            qualified = True
        else:
            qualified = False
    else:
        qualified = False
    return qualified


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00
    order = str(input("Order B - burger or W - wings:"))
    if order == "B":
        order_price = BURGER
    else:
        order_price = WINGS
    combo = str(input("Make it a combo? (Y/N):"))
    if combo == "Y":
        combo_choice = str(input("Add F - fries or S - salad:"))
        if combo_choice == "F":
            combo_price = FRIES
        else:
            combo_price = SALAD
        price = order_price + combo_price
    else:
        price = order_price
    return price
