#!/usr/bin/python3
"""write an object to a text file using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file."""
    with open(filename, 'w') as outfile:
        json.dump(my_obj, outfile)
