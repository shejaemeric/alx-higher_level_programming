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
        area = self.area()
        if area == 0:
            print()
        for i in range(0, area):
            for y in range(0, area):
                print('#', end="")
