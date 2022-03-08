"""
-------------------------------------------------------
Lab 6, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-29"
-------------------------------------------------------
"""


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for x in range(2, num + 1, 2):
        total = total + x
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    num = height * 2
    if len(char) == 1 and height > 0:
        for x in range(1, num, 2):
            print((height - 1) * " " + x * char)
            height = height - 1
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    if (start + end) % inc != 0:
        for x in range(start, end, inc):
            num1 = burnt_per_minute * x
            print(f"Calories burned after {x:d} minutes: {num1:.1f}")
    else:
        for y in range(start, end + inc, inc):
            num1 = burnt_per_minute * y
            print(f"Calories burned after {y:d} minutes: {num1:.1f}")
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    if value > 0 and years > 0 and rate > 0:
        print(f"Year       Value $")
        print(f"------------------")
        print(f" 0 {value:15,.2f}")
        for x in range(0 + 1, years + 1):
            value = value + (value * (rate / 100))
            final_value = value
            print(f"{x:^3d}{final_value:15,.2f}")
    return final_value


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    if (n > 0):
        x = 0
        total = 0
        firstv = float(input("First value:"))
        maximum = firstv
        minimum = firstv
        total = firstv
        for x in range(0, n - 1, 1):
            next_v = float(input("Next value:"))
            total = total + next_v
            x = x + 1
            if next_v < minimum:
                minimum = next_v
            elif next_v > maximum:
                maximum = next_v
        average = total / n
    return minimum, maximum, total, average
