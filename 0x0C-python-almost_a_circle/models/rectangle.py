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

    def display(self):
        """display the rectangle"""
        print(('\n' * self.__y) + '\n'.join(((' ' * self.__x) +
                                             ('#' * self.__width))
                                            for i in range(self.__height)))

    def __str__(self):
        """overiding str function"""
        return "[Rectangle] ({self.id}) {self.x}/{self.y}"\
            .format(self=self) + " - {self.width}/{self.height}"\
            .format(self=self)

    def update(self, *args, **kwargs):
        """Update class using *args or **kwargs"""
        index = 0
        if len(args) > 1:
            for arg in args:
                if index == 0:
                    super().__init__(args[index])
                elif index == 1:
                    self.width = args[index]
                elif index == 2:
                    self.height = args[index]
                elif index == 3:
                    self.x = args[index]
                elif index == 4:
                    self.y = args[index]
                index += 1
            return
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """return rectangle dictionary"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
