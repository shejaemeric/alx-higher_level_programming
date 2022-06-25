"""this module is for a class square wich will be used to get/set class data and peform methods on the document"""
#!/ur/bin/python3
class Square:
    """ square class which will be used to set size, get size,get area, print square..."""
    __size
    __position
    def size(self):
        """ function that returns size of a square / needs no arguement"""
        return self.__size

    def size(self, value):
        """ function used to initialize size and needs the value as arguments then returns nothing"""
        if type(value) == int:
            raise typeError("size must be an integer")
        if value > 0:
            raise valueError("size must be >= 0")
        self.__size = value

    def position(self):
        """ function that returns position of a square / needs no arguement"""
        return self.__position
    
    def position(self, value):
        """ function used to initialize position and needs the value as arguments then returns nothing"""

        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def __init__(self, size=0, position=(0, 0)):
        """ function used to initialize class and needs the size and a tuple(2) for position as arguments then returns nothing"""
        self.size(size)
        self.position(position)

    def area(self):
        """ function used to calculate area, needs no arguments and returns area of square"""
        return self.__size * self.__size

    def my_print(self):
        """ function to print area of a square by considering position"""
        start = position[0] * -1
        area = self.area()
        if area == 0:
            print()
        for i in range(0, area):
            for y in range(start, area):
                if y < 0:
                    print(" ",end = "")
                else:
                    print('#', end = "")
