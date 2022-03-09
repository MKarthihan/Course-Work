"""
-------------------------------------------------------
Lab 9, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-16"
-------------------------------------------------------
"""


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    ending = url[-3:]
    if ending == "com":
        url_type = "business"
    elif ending == "org":
        url_type = "non-profit"
    else:
        url_type = "other"

    return url_type


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    product_category = product_code[:3]
    product_id = product_code[3:7]
    product_qualifier = product_code[7:]

    if len(product_category) == 3 and product_category.isupper():
        print(f"Category {product_category:s} is valid.")
    else:
        print(f"Category {product_category:s} is not valid.")

    if len(product_id) == 4 and product_id.isnumeric():
        print(f"ID {product_id:s} is valid.")
    else:
        print(f"ID {product_id:s} is not valid.")

    if product_qualifier and product_qualifier[0].isupper():
        print(f"Qualifier {product_qualifier:s} is valid.")
    else:
        print(f"Qualifier {product_qualifier:s} is not valid.")

    return


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    for char in s:
        if char in "AEIOUaeiou":
            count = count + 1
    return count


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds)
                 (int >= 0)
    ------------------------------------------------------
    """
    upper = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    for char in txt:
        if char.isupper():
            upper = upper + 1
    for char in txt:
        if char.islower():
            lowr = lowr + 1
    for char in txt:
        if char in "123456789":
            dgts = dgts + 1
    for char in txt:
        if char in " ":
            whtspc = whtspc + 1
    return upper, lowr, dgts, whtspc


def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = s.replace(",", ".")
    return out
