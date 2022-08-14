#!/usr/bin/python3
"""module for student class"""


class Student:

    """ class for student object """

    def __init__(self, first_name, last_name, age):

        """__init__ :initialize class

        Args:
            first_name (string): first_name of student
            last_name (string): last_name of student
            age (string): age of student
        """
        self.irst_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """
            to_json return dictionary representation of object.
        """
        return self.__dict__
        