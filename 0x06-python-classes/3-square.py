"""this module is for a class square"""
#!/usr/bin/python3


class Square:
    """ square class which will be used to set size, 
    get size,get area, print square..."""
     __size
    def __init__ (self,size =0):
        """ function used to initialize class and needs 
        the size as arguments then returns nothing"""
        if type(size) == int:
            raise typeError("size must be an integer")
        if size > 0:
            raise valueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ function used to calculate area, needs no 
        arguments and returns area of square"""
        return self.__size * self.__size
