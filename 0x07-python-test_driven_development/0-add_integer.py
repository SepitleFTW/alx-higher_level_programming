#!/usr/bin/python3

def add_integer(a, b=98):

    if type(a) != int:
        raise TypeError("a must be an integer")

    if type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int:
        raise TypeError("b must be an integer")

    if type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b == int(b)

    return a + b