#!/usr/bin/python3
"""Square module."""


class Square:
    """defines a square"""

    __size
    __position

    def size(self):
        """Properties for the length of a sise of a square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size

    def size(self, value):
        """setter function for private attribute size.
           Args:
                value: size value to set to.
        """
        if type(value) != int:
            raise typeError("size must be an integer")
        if value > 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def position(self):
        """Property for square position.
        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    def position(self, value):
        """setter function for private attribute position
           Args:
                value: position value to set to.
        """

        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size(int): length of side of the square.
            position(int tuple): position of the square
        """
        self.size(size)
        self.position(position)

    def area(self):
        """Area of the square.
        Returns:
            thee size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints square with char #"""
        start = position[0] * -1
        area = self.area()
        if area == 0:
            print()
        for i in range(0, area):
            for y in range(start, area):
                if y < 0:
                    print(" ", end="")
                else:
                    print('#', end="")
