#!/usr/bin/python3
"""
class of square that defines a square
"""


class Square:
    """
    class of square that defines a square
    """
    def __init__(self, size):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self, value):
        self.value = value
