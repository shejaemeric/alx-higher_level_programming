#!/usr/bin/python3
"""
    module for BaseGeometry class
"""


class BaseGeometry:

    """
        class for BaseGeometry attributes
    """
    def area(self):

        """
            area: raises an exception that the area function has not been
            implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        integer_validator validates value

        Args:
            name (string): always string
            value (int): must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")
            