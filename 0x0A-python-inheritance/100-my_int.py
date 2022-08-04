#!/usr/bin/python3
"""
    module for MyInt(a rebel for int class)
"""


class MyInt(int):

    """
    MyInt: class which is a rebel of Int class

    Args:
        Int (Class): Integer class
    """
    def __eq__(self, otherInt):

        """
        __eq__: Overriding equal function of my int

        Args:
            otherInt (Int): Other int to compare
        """
        return self != otherInt

    def __nq__(self, otherInt):

        """
        __nq__: Overriding not equal function of my int

        Args:
            otherInt (Int): Other int to compare
        """
        return self == otherInt
