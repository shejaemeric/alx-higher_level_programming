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
        __width = width
        __height = height
