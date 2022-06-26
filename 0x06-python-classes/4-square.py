#!/usr/bin/python3
"""Square module."""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Constructor.
        Args:
            size: length of side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        self.__size = size

    @Property
    def size(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size ** 2
