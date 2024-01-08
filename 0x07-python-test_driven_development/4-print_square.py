#!/usr/bin/python3
"""a square printing funct"""

def print_square(size):
    """prints squares using #s """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for a in range(size):
        for b in range(size):
            print('#', end='')
        print()
