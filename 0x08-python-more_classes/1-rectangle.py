#!/usr/bin/python3
"""rectangle class that will define a rectangle
"""


class Rectangle:
    """Rect angle class
    """
    def __init__(self, width=0, height=0):
        """constructor
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """property setter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
