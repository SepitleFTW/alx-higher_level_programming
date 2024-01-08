#!/usr/bin/python3
""" text indentation func"""

def text_indentation(text):
    """ new line starts after '.' '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

def print_text(text):
    """ prints new text """
    for char in text:
        print(char, end="")

        if char in ".?:":
            print("\n\n")



