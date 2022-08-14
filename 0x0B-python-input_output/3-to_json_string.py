#!/usr/bin/python3
import JSON

""" module for a function that returns json string of an object"""


def to_json_string(my_obj):

    """to_json_string : converts object to json string.

    Args:
        my_obj (object): object to convert
    """

    return JSON.dumps(my_obj)
