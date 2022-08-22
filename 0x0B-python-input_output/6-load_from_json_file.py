#!/usr/bin/python3
""" module for load_from_json_file function """


import json


def load_from_json_file(filename):

    """load_from_json_file: creates an object from a json file.

    Args:
        filename (file): json file
    """
    with open(filename, 'r') as f_obj:
        data = f_obj.read()
        return json.loads(data)
