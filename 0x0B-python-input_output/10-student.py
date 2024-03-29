#!/usr/bin/python3
"""class Student that defines them by 9-student.py"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Construct for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a JSON representation of student"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict_
