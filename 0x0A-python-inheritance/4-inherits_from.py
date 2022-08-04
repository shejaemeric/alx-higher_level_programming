#!/usr/bin/python3
"""
    module for is_kind_of_class function
"""


def inherits_from(obj, a_class):

    """
    inherits_from :  returns True if the object is an instance of a class that /
    inherited (directly or indirectly) from the specified class /
    ;otherwise False.

    Args:
        obj (class instance): object to check
        a_class (class) : class to check against
    """
    return issubclass(obj, a_class)
