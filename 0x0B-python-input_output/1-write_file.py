#!/usr/bin/python3
""" write text to file"""


def write_file(filename="", text=""):
    """ write text to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

