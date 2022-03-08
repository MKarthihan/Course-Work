"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-14"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings that
    represent the output of a game with a loop
    Use: team1, team2 = winner()
    -------------------------------------------------------
    Parameters:
        No parameters
    Returns:
        team1 - number of wins (int >=0)
        team2 - number of wins (int >=0)
    ------------------------------------------------------
    """
    team1 = 0
    team2 = 0
    point = input("Enter the winning team:")
    while point != "":
        if point == "blue":
            team1 += 1
            point = input("Enter the winning team:")
        elif point == "grey":
            team2 += 1
            point = input("Enter the winning team:")

    print("")
    print(f"Blue:{team1:d} Grey:{team2}")
    if team1 > team2:
        print("Blue is the winner!")
    elif team2 > team1:
        print("Grey is the winner!")
    elif team1 == team2:
        print("Blue & Grey (TIE)")

    return team1, team2


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime_barrier = 2
    while num % prime_barrier != 0:
        prime_barrier += 1
        if prime_barrier == num:
            prime = True
        elif prime_barrier < num:
            prime = False
    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    time = 0
    leftover_money = principal
    print(f"Principal:    ${principal:.2f}")
    print(f"Interest Rate:    {rate:.1f}%")
    print(f"Monthly Payment:   ${payment:.2f}")
    print(f"------------------------------------")
    print(f"Month   Interest   Payment   Balance")
    print(f"------------------------------------")
    while leftover_money > 0:
        time += 1
        bracket = ((rate / 100) * leftover_money)
        interest = bracket / 12
        leftover_money += interest
        if leftover_money - payment > 0:
            leftover_money -= payment
        else:
            payment = leftover_money
            leftover_money = 0
        print(f"{time:>5d}{interest:>10.2f}{payment:>10.2f} {leftover_money:>10.2f}")
    return


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 0
    if num == 0:
        count = 1
    if num < 0:
        num *= -1
    while num != 0:
        count += 1
        num = num // 10
    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 1
    start_num = num
    for x in range(2, (int(num**(1 / 2)) + 1)):
        sum1 = 1
        placement = 1
        while num % x == 0:
            num = num / x
            placement = placement * x
            sum1 += placement
        total = total * sum1
    if num > 2:
        total = total * (1 + num)
    total = total - start_num
    return total
