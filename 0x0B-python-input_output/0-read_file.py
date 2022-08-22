#!/usr/bin/python3
""" module for read file function """


def read_file(filename=""):

    """
    read_file: reads a file and display it's content to stdout

    Args:
        filename (str, optional): name of the flile. Defaults to "".
    """

    with open(filename, 'r', encoding='UTF8') as F_obj:
        read_data = F_obj.read()
        print(read_data, end='')
