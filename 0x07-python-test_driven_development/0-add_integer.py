#!/usr/bin/python3
"""module for 0-add_integer
"""

def add_integer(a, b=98):
    """ adds 2 numbers
    """

    if ((not isinstance(type(a), int))):
       raise TypeError("a must be an integer")

    if ((not isinstance(type(a), float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(type(b), int))):
        raise TypeError("b ust be an integer")

    if ((not isinstance(type(b), float))):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return (int(a) + int(b))
