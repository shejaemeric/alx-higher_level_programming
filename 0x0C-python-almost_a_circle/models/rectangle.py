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
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width"""
        return self.__width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @property
    def x(self):
        """returns x"""
        return self.__x

    @property
    def y(self):
        """returns y"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets width value

        Args:
            value (int): value to assign to width
        """
        self.setter_validation('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """sets x value

        Args:
            value (int): value to assign to x
        """
        self.setter_validation('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        """sets y value

        Args:
            value (int): value to assign to y
        """
        self.setter_validation('y', value)
        self.__y = value

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """return area of rectangle"""
        return self.__height * self.__width
