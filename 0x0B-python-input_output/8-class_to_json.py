#!/usr/bin/python3
"""return dict with simple data struct for JSON serialization"""


def class_to_json(obj):
    """convert a class to JSON"""
    return obj.__dict__
