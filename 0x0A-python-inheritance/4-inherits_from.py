#!/usr/bin/python3
""" true if obj is instance of class inherited
directly or indirectly from the specified class"""

def inherits_from(obj, a_class):
    """obj is object to check, a_class is to match obj too """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
