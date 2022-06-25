"""this module is for a class square wich will be used to get/set 
class data and peform methods on the document"""
#!/usr/bin/python3


class Square:
    """ square class which will be used to set size, get size,
    get area, print square..."""
    __size
    def __init__ (self,size =0):
        """ function used to initialize class and needs the size 
        as arguments then returns nothing"""
        self.__size = size
