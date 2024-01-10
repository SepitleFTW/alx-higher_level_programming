#!/usr/bin/python3
"""read a file from the given filename"""

def read_file(filename=""):
    """read a file from the given filename"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
