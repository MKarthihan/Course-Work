"""
-------------------------------------------------------
Functions
-------------------------------------------------------
Author:  Karthihan Maheswaran
ID:      210743860
Email:   mahe3860l@mylaurier.ca
__updated__ = "2022-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())
    while not source1.is_empty():
        target.push(source1.pop())
    while not source2.is_empty():
        target.push(source2.pop())
    return target

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = []
    while not source.is_empty():
        lst.append(source.pop())
    while len(lst) > 0:
        source.push(lst.pop(0))
    return
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    empty = ""
    for char in string:
        if char.isalpha():
            empty = empty + char.lower()
    length = len(empty)
    incre = 0
    stack = Stack()
    while incre < (length//2):
        stack.push(empty[incre]) 
        incre += 1
    if length % 2 == 0:
        incre = (length//2)
    else: 
        incre = (length//2) + 1
    while palindrome and incre < length:
        if empty[incre] != stack.pop():
            palindrome = False
        else:
            incre += 1
    return palindrome
    
    
    
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    length_op = len(opstring)
    length_val = len(values_in)
    stack = Stack()
    values_out= []
    incre_1 = 0
    incre_2 = 0
    while values_out is not incre_1 < length_op:
        if opstring[incre_1] == "S" and incre_2 < length_val:
            stack.push(values_in[incre_2])
            incre_2 += 1
        elif opstring[incre_1] == "X" and not stack.is_empty():
            values_out.append(stack.pop())
        else:
            values_out = None
        incre_1 += 1
    if incre_2 < length_val:
        values_out = None
    return values_out