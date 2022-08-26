#!/usr/bin/python3
""" rectangle module"""
from models.base import Base


class Rectangle(Base):

    """
    rectangle class

    Args:
        Base (class): base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """initialize rectangle class

        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns width"""
        return self.__height

    @property
    def x(self):
        """returns width"""
        return self.__x

    @property
    def y(self):
        """returns width"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets width value

        Args:
            value (int): value to assign to width
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height value

        Args:
            value (int): value to assign to height
        """
        self.__height = value

    @y.setter
    def y(self, value):
        """sets x value

        Args:
            value (int): value to assign to x
        """
        self.__x = value

    @x.setter
    def x(self, value):
        """sets x value

        Args:
            value (int): value to assign to x
        """
        self.__x = value
