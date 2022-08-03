#!/usr/bin/python3
"""
print a square using #
"""


def print_square(size):
    """
    print_square: prints a squre using '#'

    Args:
        size (int): size of a square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
 
    for height in range(0, size):
        for width in range(0, size):
            print("#", end="")
        print()
