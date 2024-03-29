#!/usr/bin/python3
"""
    module for Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
        class for Rectangle attributes: inherit BaseGeometry class
    """

    def __init__(self, width, height):

        """__init__ : initialize class

        Args:
            width (int): width of rectangle
            height (int): height of a rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        """
        area: Return area of rectangle.

        Return (int): area of rectangle.
        """

        return self.__width*self.__height

    def __str__(self):

        """
        __str__ : return rectangle representation
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
