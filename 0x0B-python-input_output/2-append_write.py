#!/usr/bin/python3
""" module for write at the end of a file function """


def append_write(filename="", text=""):

    """
    append_write: creates a file if it does not exists /
    and wites at the end of it

    Args:
        filename (str, optional): name of the flile. Defaults to "".
        text (str,optional): text to write in file. Defaults to "".
    """
    with open(filename, 'a', encoding='UTF8') as F_obj:
        write_data = F_obj.write(text)
        return write_data
