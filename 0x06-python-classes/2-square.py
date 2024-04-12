#!/usr/bin/python3
"""
a class square that defines a square
"""


class Square:
    """
    a class square that defines a square
    """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be a positive integer")
