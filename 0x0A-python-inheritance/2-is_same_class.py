#!/usr/bin/python3
"""
    module for 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    is_same_class : checks if an object is an instance of a class

    Args:
        obj (class_instance): object to check
        a_class (class): class to check
    """
    return type(obj) == a_class
    