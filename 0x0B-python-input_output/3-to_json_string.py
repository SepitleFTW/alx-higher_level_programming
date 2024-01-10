#!/usr/bin/python3
"""a func that returns JSON repr of a string"""
import json

def to_json_string(my_obj):
    """Returns a JSON string representation of an object."""

    return json.dumps(my_obj)
