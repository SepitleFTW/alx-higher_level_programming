#!/usr/bin/python3
"""is instance equal or not?"""

def is_kind_of_class(obj, a_class):
    """ is it kind of a class"""
    if isinstance(obj, a_class):
        return True
    return False
