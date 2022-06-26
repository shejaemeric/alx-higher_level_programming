#!/usr/bin/python3
"""Square module."""


class Square:
    """defines a square"""

    __size

    def size(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size

    def size(self, value):
        """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if type(value) != int:
            raise typeError("size must be an integer")
        if value > 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if type(size) != int:
            raise typeError("size must be an integer")
        if size > 0:
            raise valueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size * self.__size
