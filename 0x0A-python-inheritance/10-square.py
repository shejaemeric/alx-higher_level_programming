#!/usr/bin/python3
"""
    Module for square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Square _summary_

    Args:
        Rectangle (class): inherited class
    """

    def __init__(self, size):

        """
        __init__: initiates class square.

        Args:
            size (int): size of square.
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
