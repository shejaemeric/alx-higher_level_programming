#!/usr/bin/python3
""" module for loads add and save json """


import sys

save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

items = load_json('add_item.json')
for x in sys.argv:
    items.append(x)

save_json(items, 'add_item.json')
