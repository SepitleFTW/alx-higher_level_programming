#!/usr/bin/python3
""" funciton that appends string at end of file"""


def append_write(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
