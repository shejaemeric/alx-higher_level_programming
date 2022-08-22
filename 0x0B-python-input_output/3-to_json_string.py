#!/usr/bin/python3
""" module for a function that returns json string of an object"""


import json


def to_json_string(my_obj):

    """to_json_string : converts object to json string.

    Args:
        my_obj (object): object to convert

    Returns:
        JSON string
    """

    return json.dumps(my_obj)
