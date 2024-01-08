#!/usr/bin/python3
"""module for 0-add_integer
"""

def add_integer(a, b=98):
    """ adds 2 numbers
    """

    if ((not isinstance(a, int))):
       raise TypeError("a must be an integer")

    if ((not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int))):
        raise TypeError("b ust be an integer")

    if ((not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
