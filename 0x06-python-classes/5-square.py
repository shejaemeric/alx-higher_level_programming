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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square.
        Returns:
            the size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
