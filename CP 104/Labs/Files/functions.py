"""
-------------------------------------------------------
Lab 10, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-11-26"
-------------------------------------------------------
"""


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline()
    count = 0
    while line != "" and count < n:
        count += 1
        line = fh.readline()
    if line != "":
        result = line.strip().split(",")

    return result


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = (fh.readline())
    index = 0
    while line != "" and index != 1:
        if id_number in line:
            result = line.strip().split(",")
            index = 1
        else:
            line = (fh.readline())
    return result


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()
    first = int(line.strip())
    smallest = first
    largest = first
    total = first
    counter = 1
    line = fh.readline()
    while line != "":
        counter += 1
        second = int(line.strip())
        if smallest > second:
            smallest = second
        if largest < second:
            largest = second
        total += second
        line = fh.readline()
    average = total / counter
    return smallest, largest, total, average


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    count = 0
    line = fh.readline()
    while line != "":
        if value == int(line):
            count = count + 1
        line = fh.readline()
    return count


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline()
    word = line.strip()
    while line != "":
        line = line.strip()
        if len(line) < len(word):
            word = line
        line = fh.readline()
    return word
