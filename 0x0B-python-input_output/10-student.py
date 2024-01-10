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
        if attrs is None:
            attrs = self.__dict__
        return json.dumps(attrs, default=class_to_json)
