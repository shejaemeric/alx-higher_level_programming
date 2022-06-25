#!/usr/bin/python3
"""this module is for a class square"""


class Square:
    """ square class which will be used to set size, get size,
    get area, print square..."""
    __size
    def __init__ (self,size =0):
        """initialize class and needs the size
        as arguments then returns nothing
        """
        self.__size = size
