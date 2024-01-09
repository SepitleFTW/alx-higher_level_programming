#!/usr/bin/python3
""" write basegeometry based on question 6"""

class BaseGeometry:
    """empty class"""

    def area(self):
        """ raise the below typerror"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """init and set values"""

        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

