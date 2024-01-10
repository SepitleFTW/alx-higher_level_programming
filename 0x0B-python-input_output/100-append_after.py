#!/usr/bin/python3
"""inserts line of text after each line with specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inseert comment here later im sleepy"""
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            if search_string in line:
                lines.append(line)
                lines.append(new_string)
            else:
                lines.append(line)  #
    with open(filename, 'w') as file:
        """inseert comment here later im sleepy"""

        for line in lines:
            file.write(line)
