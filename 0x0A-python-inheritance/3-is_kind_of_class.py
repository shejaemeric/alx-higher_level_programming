#!/usr/bin/python3
"""
    module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):

    """
    eturns True if the object is an instance of, or if the object is an instance /
    of a class that inherited from, the specified class ; otherwise False.

    Args:
        obj (class_instance): object to check
        a_class (class): class to check
    """
    return isinstance(obj,a_class)
