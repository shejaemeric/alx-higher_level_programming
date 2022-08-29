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
