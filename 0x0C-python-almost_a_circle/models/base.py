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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file of obj

        Args:
            list_objs (list): a list of instances who inherits of Base
        """
        lo = []
        name = cls.__name__ + ".json"
        if list_objs is not None:
            for item in list_objs:
                lo.append(cls.to_dictionary(item))
        with open(name, 'w') as F:
            F.write(cls.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """deserialize a jason string

        Args:
            json_string (_type_): _description_
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from json file"""
        name = cls.__name__ + ".json"
        if !(name e):
            return []
        with open(name,'r') as F:
            str = F.read()
        return cls.from_json_string(str)

Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

The filename must be: <Class name>.json - example: Rectangle.json
If the file doesn’t exist, return an empty list
Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
You must use the from_json_string and create methods (implemented previously)
