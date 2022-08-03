#!/usr/bin/python3
"""
    module for MyList class and its attributes
"""
class MyList(list):

    """MyList class

    Args:
        List (class): inherit from list class
    """
    def print_sorted(self):
        """
            print_sorted : prints sorted list.

            Args: self object

            Return: None

        """
        for c in self:
            if not isinstance(c, int):
                raise TypeError("Element of a list must be an integer")
        self.sort()
        print(self)
