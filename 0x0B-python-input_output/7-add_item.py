#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys

if __name__ == "__main__":
    save_json = __import__("5-save_to_json_file").save_to_json_file
    load_json = __import__("6-load_from_json_file").load_from_json_file

    try:
        items = load_json("add_item.json")
    except FileNotFoundError:
        items = []

    for x in sys.argv:
        items.append(x)

    save_json(items, 'add_item.json')
