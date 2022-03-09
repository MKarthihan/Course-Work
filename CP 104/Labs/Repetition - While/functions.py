"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-04"
-------------------------------------------------------
"""
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    guess = 0
    count = 0
    number = randint(1, high)

    while guess != number:
        count += 1
        guess = int(input("Guess:"))

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        elif guess == number:
            print("Congratulations - good guess!")
            break
    return count


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    rate = (rate / 100)

    while target > current:
        current = current + (current * rate)
        years = years + 1

    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    count = 0
    total = 0
    number = float(input("First positive value:"))
    minimum = number
    maximum = number
    while number >= 0:
        total = number + total
        count = count + 1
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
        number = float(input("Next positive value:"))
    average = total / count
    return minimum, maximum, total, average


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    day = 1
    days_away = "Y"
    b_total = 0
    l_total = 0
    s_total = 0

    while days_away == "Y":
        print(f"Day {day}")
        print()

        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))

        b_total += breakfast
        l_total += lunch
        s_total += supper

        total = breakfast + lunch + supper

        print(f"Your total for the day was ${total:.2f}")
        print()
        days_away = input("Were you away another day (Y/N)? ")
        print()

        day += 1

    a_total = b_total + l_total + s_total

    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low:d} and high {high:d}:"))
    while value > high or value < low:
        if value > high:
            print("Value entered is too high")
        elif value < high:
            print("Value entered is too low")
        value = int(input(f"Enter a value between {low:d} and high {high:d}:"))
    print("")
    return value
