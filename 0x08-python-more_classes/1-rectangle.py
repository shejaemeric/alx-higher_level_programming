#!/usr/bin/python3
"""this is a module for a rectangle class"""


class Rectangle:
    """
    my rectangle class.

    Atrributes:
        width (int): rectangle width.
        height (int): rectangle height.
    """

    def __init__(self,width = 0,height = 0):
        """
        initialize class

        Args:
            width (int): rectangle width.
            height (int): rectangle height.

        """
        self.width = width
        self.height = height

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
        if not isinstance(value,int):
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
    def width(self, value):
        """
        sets width property
        Args:
            value (int) : width of the ractangle
        Raise:
            TypeError : if width is not an integer
            ValueError : if width is less than zero
        """
        if isinstance(value,int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
