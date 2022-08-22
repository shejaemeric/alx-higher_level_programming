#!/usr/bin/python3
""" module for write file function """


def write_file(filename="", text=""):

    """
    write_file: creates a file if it does not exists and wites to it

    Args:
        filename (str, optional): name of the flile. Defaults to "".
        text (str,optional): text to write in file. Defaults to "".
    """
    with open(filename, 'w', encoding='UTF8') as F_obj:
        write_data = F_obj.write(text)
        return write_data
