#!/usr/bin/python3
""" documentation for base module"""

class Base:
    """class for base data and members"""
    
    
    __nb_objects = 0
    
    def __init__(self,id=None):
        
        """ 
        initialize class

        Args:
            id (int, optional): _id of base_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
