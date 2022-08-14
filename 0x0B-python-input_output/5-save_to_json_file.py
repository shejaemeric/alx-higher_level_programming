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

    my_str = json.dumps(my_obj)

    with open(filename, 'w', encoding='UTF8') as f_obj:
        f_obj.write(my_str)
