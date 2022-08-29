#!/usr/bin/python3
""" documentation for base module"""


import json


class Base:
    """class for base data and members"""

    __nb_objects = 0

    def __init__(self, id=None):

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation"""
        if list_dictionaries in None:
            return []
        return json.dumps(list_dictionaries)
