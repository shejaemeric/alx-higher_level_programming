#!/usr/bin/python3
"""Square module."""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size(int): length of side of the square.
            position(int tuple): position of the square
        """
        self.__size = size

    @property
    def size(self):
        """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for private attribute size.
           Args:
                value: size value to set to.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for square position.
        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter function for private attribute position
           Args:
                value: position value to set to.
        """

        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints square with char #"""
        start = self.position[0] * -1
        if self.size == 0:
            print()
        for i in range(0, self.__size):
            for y in range(start, self.__size)):
                if y < 0:
                    print(" ", end="")
                else:
                    print('#', end="")
