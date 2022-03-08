"""
-------------------------------------------------------
Assignment 4, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-10-19"
-------------------------------------------------------
"""


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Returns a string representing the corresponding day of the week:
        "Monday" - 1
        "Tuesday" - 2
        "Wednesday" - 3
        "Thursday" - 4
        "Friday" - 5
        "Saturday" - 6
        "Sunday" - 7
    Returns "Error" if day_number is < 0 or > 7 .
    Use: result = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - Number of a day in a week (int)
    Returns:
        result - name of day in a week (str)
    ------------------------------------------------------
    """
    if day_number == 1:
        result = "Monday"
    elif day_number == 2:
        result = "Tuesday"
    elif day_number == 3:
        result = "Wednesday"
    elif day_number == 4:
        result = "Thursday"
    elif day_number == 5:
        result = "Friday"
    elif day_number == 6:
        result = "Saturday"
    elif day_number == 7:
        result = "Sunday"
    elif day_number > 7 or day_number < 1:
        result = "Error"
    return result


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if 0 <= aqi <= 50:
        level = "Good"
    elif 51 <= aqi <= 100:
        level = "Moderate"
    elif 101 <= aqi <= 150:
        level = "Unhealthy for Sensitive Groups"
    elif 151 <= aqi <= 200:
        level = "Unhealthy"
    elif 201 <= aqi <= 300:
        level = "Very Unhealthy"
    elif aqi > 300:
        level = "Hazardous"
    elif aqi < 0:
        level = "Error"
    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 >= v2 and v1 >= v3:
        if v2 > v3:
            product = v1 * v2
        elif v3 > v2:
            product = v1 * v3
    elif v2 >= v1 and v2 >= v3:
        if v1 > v3:
            product = v1 * v2
        elif v3 > v1:
            product = v2 * v3
    elif v3 >= v1 and v3 >= v2:
        if v1 > v2:
            product = v3 * v1
        elif v2 > v1:
            product = v2 * v3
        elif v2 == 0 and v3 == 0:
            product = v1
        elif v1 == 0 and v3 == 0:
            product = v2
        elif v1 == 0 and v2 == 0:
            product = v3
        elif v1 == 0 and v2 == 0 and v3 == 0:
            product = 0
    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == "red" and rgb2 == "blue" or rgb1 == "blue" and rgb2 == "red":
        colour = "fuchsia"
    elif rgb1 == "red" and rgb2 == "green" or rgb1 == "green" and rgb2 == "red":
        colour = "yellow"
    elif rgb1 == "green" and rgb2 == "blue" or rgb1 == "blue" and rgb2 == "green":
        colour = "aqua"
    elif rgb1 == "red" and rgb2 == "red":
        colour = "red"
    elif rgb1 == "blue" and rgb2 == "blue":
        colour = "blue"
    elif rgb1 == "green" and rgb2 == "green":
        colour = "green"
    elif rgb1 != "red" or "blue" or "green" or rgb2 != "red" or "blue" or "green":
        colour = "Error"
    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Returns one of the following strings
        "Yee" if number is evenly divisible by 3
        "Ha" if number is evenly divisible by 7
        "Yee Ha" if number is evenly divisible by both 3 and 7
    Returns "Nada" if number is none of the above.
    Use: result = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - a number (int)
    Returns:
        result - the string of the division (str)
    ------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 != 0:
        result = "Yee"
    elif number % 7 == 0 and number % 3 != 0:
        result = "Ha"
    elif number % 3 == 0 and number % 7 == 0:
        result = "Yee Ha"
    elif number % 3 != 0 and number % 7 != 0:
        result = "Nada"
    return result
