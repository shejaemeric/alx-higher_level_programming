#!/usr/bin/python3
""" module for a function that returns an object /
    represented by a json string
"""


import json


def from_json_string(my_str):

    """from_json_string : return an object represented by a string.

    Args:
        my_str (string): string to deserialize.

    Returns:
        object: object
    """

    return json.loads(my_str)
