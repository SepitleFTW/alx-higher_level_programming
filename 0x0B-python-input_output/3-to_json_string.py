#!/usr/bin/python3
"""a func that returns JSON repr of a string"""
import json

def to_json_string(my_obj):
    """Returns a JSON string representation of an object."""
    json_str = json.dumps(my_obj)
        return json_str
