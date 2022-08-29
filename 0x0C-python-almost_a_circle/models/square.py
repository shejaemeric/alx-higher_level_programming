#!/usr/bin/python3
"""this is square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class

    Args:
        Rectangle (class): inherited class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize square class

        Args:
            size (int): size of square
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return representation of a string"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size value

        Args:
            value (int): value to assign to size
        """
        super().setter_validation("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates an object"""
        if len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.width = args[index]
                    self.height = args[index]
                elif index == 2:
                    self.x = args[index]
                elif index == 3:
                    self.y = args[index]

                index += 1
            return
        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.width = kwargs["size"]
            self.height = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """return square dictionary"""
        d = {}
        d["id"] = self.id
        d["size"] = self.width
        d["x"] = self.x
        d["y"] = self.y
        return d
