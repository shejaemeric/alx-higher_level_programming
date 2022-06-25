#!/usr/bin/python3
"""Square module."""


class Square:
    """ square class which will be used to set size, get
    size,get area, print square..."""
    __size

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if type(size) == int:
            raise typeError("size must be an integer")
        if size > 0:
            raise valueError("size must be >= 0")
        self.__size = size
