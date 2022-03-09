"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2021-12-03"
-------------------------------------------------------
"""


def file_head(fh, linecount):
    """
    -------------------------------------------------------
    Prints first linecount lines of fh. Line numbering starts at 0.
    If length of file is shorter than linecount, stops printing after
    last line of file.
    Use: file_head(fh, linecount)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
        linecount - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line = 0
    info = fh.readline()
    while line < linecount and info != '':
        print(f'{info}', end='')
        info = fh.readline()
        line += 1
    return


def file_integers(fh):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: numbers = file_integers(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process ( (file handle - open for reading)
    Returns:
        numbers - a list of integers from fh (list of int)
    -------------------------------------------------------
    """
    lst = [(line.strip()).split("," " ") for line in fh]
    newlist = [item for innerlist in lst for item in innerlist]
    list2Str = ','.join(map(str, newlist))
    final_lst = list(list2Str.split(","))
    numbers = []
    for item in final_lst:
        for sublist in item.split():
            if(sublist.isdigit()):
                numbers.append(int(sublist))
    return numbers


def file_stats(fh):
    """
    -------------------------------------------------------
    Evaluates the contents of a file.
    Use: ucount, lcount, dcount, wcount = file_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        ucount - The number of uppercase letters in the file (int)
        lcount - The number of lowercase letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of whitespace characters in the file (int)
    -------------------------------------------------------
    """
    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    for line in fh:
        for char in line:
            if char.isdigit():
                dcount += 1
            elif char.isspace():
                wcount += 1
            elif char.isupper():
                ucount += 1
            elif char.islower():
                lcount += 1
    return ucount, lcount, dcount, wcount


def flatten(matrix):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list matrix. A 'flattened' list is a
    2D list that is converted into a 1D list by rows.
    matrix must be unchanged.
    Use: flat = matrix_flatten(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of int)
    Returns:
        flat - the flattened version of matrix (list of int)
    -------------------------------------------------------
    """
    flat = [index for sublist in matrix for index in sublist]
    return flat


def matrix_rotate_right(matrix):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: rotated = matrix_rotate_right(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2d list of int/float)
    Returns:
        rotated - the rotated version of matrix (2D list of int/float)
    -------------------------------------------------------
    """
    rotated = []
    for x in range(len(matrix[0])):
        lst = []
        for y in range((len(matrix) - 1), -1, -1):
            lst.append(matrix[y][x])
        rotated.append(lst)
    return rotated


def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        name
        street
        city
        postal code
        --
    Each address in the list of addresses is a list of the form:
    [name, street, city, postal code]
    Use: addresses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to process (file handle - open for reading)
    Returns:
        addresses - the addresses from fh (list of str)
    -------------------------------------------------------
    """
    List = fh
    addresses = []
    sub_list = []
    new_list = [s.replace("\n", "") for s in List]
    for sub_index in new_list:
        if '--' in sub_index:
            end, start = sub_index.split('--')
            sub_list.append(end)
            sub_list = [string for string in sub_list if string != ""]
            addresses.append(sub_list)
            sub_list = [start]
        else:
            sub_list.append(sub_index)
    return addresses
