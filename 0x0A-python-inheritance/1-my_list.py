#!/usr/bin/python3
""" class to inherit Mylist -> list"""

class MyList(list):
    """ printing for sorted list"""

    def print_sorted(self):
        """print list in asc order"""
        print(sorted(self))
