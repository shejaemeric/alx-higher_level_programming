#!/usr/bin/python3
"""
module to print first name and last name
"""


def say_my_name(first_name, last_name=""):

    """
    say_my_name : prints first and last name

    Args:
        first_name (string): first name to print
        last_name (str, optional): last name to print. Defaults to "".
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
