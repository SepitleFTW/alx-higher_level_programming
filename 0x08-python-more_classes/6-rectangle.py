#!/usr/bin/python3
"""class for rect
"""

class Rectangle:
    """init rect"""

    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """init rect values"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """def width"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """def height"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define area"""

        return self.width * self.height

    def perimeter(self):
        """define perim"""

        if self.height == 0 or self.width == 0:
            return 0
            return (self.height + self.width) * 2

    def __str__(self):
        """print the rect using #"""

        if self.width == 0 or self.height == 0:
            return ""

        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """ return string eval"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ print message when rect is del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
