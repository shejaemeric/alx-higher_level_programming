#!/usr/bin/python3
def add_integer(a, b=98):
    """
        function to add 2 numbers
        Args:
            a (int)
            b (int)
        Returns:
            int
    """
    if not isinstance(a,int):
        if not isinstance(a,float):
            raise TypeError("a must be an integer")
        else:
            num1 = int(a)

    if not isinstance(b,int):
        if not isinstance(b,float):
            raise TypeError("b must be an integer")
        else:
            num2 = int(b)

    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
