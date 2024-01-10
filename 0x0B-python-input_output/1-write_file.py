#!/usr/bin/python3
""" a function writing string to utf8 and
returns chars when written"""

def write_file(filename="", text=""):
    """ write text to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

