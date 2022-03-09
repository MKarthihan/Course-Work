"""
-------------------------------------------------------
Assignment 1, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    value = []
    for num in values:
        if num not in value:
            value.append(num)
    values.clear()
    values.extend(value)
    print(f"Cleaned: {value}")


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = ['a','e','i','o','u']
    out = [vowel for vowel in s if vowel.lower() not in vowels]
    out = ''.join(out)
    return out

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0 
    l = 0 
    d = 0 
    w = 0 
    r = 0 
    for x in fv.read():
        if x.isupper():
            u += 1
        elif x.islower():
            l += 1
        elif x.isdigit():
            d += 1 
        elif x == " ":
            w += 1
        else: 
            r += 1 
    return u, l, d, w, r 

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    if year > 0:
        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            leap_year = True
        else:
            leap_year = False
    return leap_year

def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = False
    s = s.lower()
    if s == s[::-1]:
        palindrome = True
    else:
        palindrome = False
    return palindrome

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    lst = []
    if len(a) > 0:
        for x in range(len(a)-1):
            subtraction = abs(a[x+1]-a[x])
            lst.append(subtraction)
    elif len(a) == 0:
        mb = 0 
    md = max(lst)    
    return md

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for x in range(len(a[0])):
        b.append([])
        
    for x in range(len(a)):
        for y in range(len(a[0])):
            b[y].append(a[x][y])
    return b

def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    element = [number for sublist in a for number in sublist]
    small = min(element)
    large = max(element)
    total = sum(element)
    average = total / len(element)
    return small, large, total, average

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    vowels = "aeiou"
    capital = False
    if word[0].isupper():
        capital = True
    if word[0] in vowels:
        pl = word + "way"
    else:
        char = ""
        leftover = ""
        for x in word:
            if x in (vowels + "y"):
                leftover += x
            else:
                char += x
        if capital:
            pl = leftover[0].capitalize() + leftover[1:].lower() + char.lower() + "ay"
        else:
            pl = leftover + char.lower() + "ay" 
    return pl

    
    
            
        
        
       
    
    