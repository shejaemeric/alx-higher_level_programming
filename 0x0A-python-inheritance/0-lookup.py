#!/usr/bin/python3
"""
     module for the lookup function
"""


def lookup(obj):

    """lookup : return list of all attributes in function

    Args:
        obj (class_object): object to check

    Returns:
        List: list of all atributes related to class
    """
    return dir(obj)
