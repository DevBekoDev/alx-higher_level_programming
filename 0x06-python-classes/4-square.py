#!/usr/bin/python3

"""square class

    defining class args
"""


class Square:
    """class square

    defining class args

    """

    @property
    def size(self):
        """size of sqaure
        return the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """size of the square

        return the size of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0):
        """square has a size

        the size of the square

        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area of a square

        area = size ** 2
        """

        return (self.__size ** 2)
