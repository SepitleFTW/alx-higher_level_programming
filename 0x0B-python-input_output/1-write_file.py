#!/usr/bin/python3
""" write text to file"""


def write_file(filename="", text=""):
    """ write text to file

    Args:
        filename (str): file name
        text (str): text to write
    Returns:
        number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

