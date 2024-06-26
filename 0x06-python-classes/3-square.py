#!/usr/bin/python3
"""
class square that defines a square
"""


class Square:
    """
    class square that defines a square
    """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        this will return area of square
        """
        return self.__size ** 2
