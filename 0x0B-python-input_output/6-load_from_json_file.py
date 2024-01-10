#!/usr/bin/python3
"""create an object from json file"""
import json


def load_from_json_file(filename):
    """loads an obj from JSON file"""
    with open(filename) as f:
        return json.load(f)
