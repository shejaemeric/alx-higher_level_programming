#!/usr/bin/python3
""" module for a save_to_json_file function """


import json


def save_to_json_file(my_obj, filename):

    """
    save_to_json_file : serialize and save to json file.

    Args:
        my_obj (object): obj to convert to json
        filename (file): json file

    """
    with open(filename, 'w') as f_obj:
        f_obj.write(json.dumps(my_obj))
