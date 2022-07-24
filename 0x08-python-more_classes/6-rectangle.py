#!/usr/bin/python3
"""this is a module for a rectangle class"""


class Rectangle:
    """
    my rectangle class.

    Atrributes:
        width (int): rectangle width.
        height (int): rectangle height.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        initialize class

        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        return width property
        Returns:
            width (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width property
        Args:
            value (int) : width of the ractangle
        Raise:
            TypeError : if width is not an integer
            ValueError : if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return height property
        Returns:
            height (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets width property
        Args:
            value (int) : width of the ractangle
        Raise:
            TypeError : if width is not an integer
            ValueError : if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate area of a rectangle
        Returns:
            area (int) : area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        calculate perimeter of a rectangle
        Returns:
            area (int) : perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """
        prints the rectangle with #
        """
        rect = []
        for x in range(0, self.height):
            for y in range(0, self.width):
                rect.append('#')
            if x != self.height-1:
                rect.append('\n')
        return ''.join(rect)

    def __repr__(self):
        """
        returns a string represantation
        Returns:
            string
        """
        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)

    def __del__(self):
        """
        prints Bye rectangle... when an instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
