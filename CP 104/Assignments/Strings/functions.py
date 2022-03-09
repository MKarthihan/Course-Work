"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    stringlist = []
    stringlist.append(string)
    stringlist2 = []
    for element in stringlist:
        double = [[]]
        for char in element:
            if char.isupper():
                double.append([])
            double[-1].append(char)
        stringlist2.append(' '.join(''.join(element) for element in double))
        new_string = ""
        for element in stringlist2:
            new_string += element
            new_string_1 = new_string[1].capitalize()
            new_string_2 = new_string[2:].lower()
            new_string = new_string_1 + new_string_2
            new_string = new_string.lstrip()
    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """
    ending1 = string[-1:]
    ending2 = string[-2:]
    if ending1 == "y":
        if ending2 == "ay" or ending2 == "oy":
            plural = string + "s"
        else:
            plural = string.replace(ending1, "ies", 1)
    elif ending1 == "s":
        plural = string + "es"
    elif ending2 == "sh" or ending2 == "ch":
        plural = string.replace(ending2, "es", 1)
    else:
        plural = string + "s"
    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """
    while not string2.endswith(string1):
        string1 = string1[1:]
        common = string1
    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = False
    if len(isbn) == 17:
        nums = isbn.replace("-", "")
        if len(nums) == 13:
            dashonly = ''.join([i for i in isbn if not i.isdigit()])
            if dashonly == "----":
                dash_list = list(dashonly)
                num_list = isbn.split("-")
                result = [x for x in num_list if x not in ""]
                num_list.clear()
                num_list.extend(result)
                for x in range(len(num_list)):
                    numindex = x
                    if numindex == 4:
                        newisbn = num_list[0], dash_list[0], num_list[1], dash_list[
                            1], num_list[2], dash_list[2], num_list[3], dash_list[3], num_list[4]
                        newlist = list(newisbn)
                        for i in range(len(newisbn)):
                            newindex = i
                            if newindex == 8:
                                if newlist[1] == "-" and newlist[3] == "-" and newlist[5] == "-" and newlist[7] == "-":
                                    if newlist[0] == "978" or newisbn[0] == "979":
                                        endingdash = isbn[-2]
                                        if endingdash == "-":
                                            valid = True
    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    lst = []
    lst.append(word_list[0])
    word_chain = False
    for word in word_list:
        for char in word[0]:
            if char == lst[-1][-1]:
                word_chain = True
    return word_chain
