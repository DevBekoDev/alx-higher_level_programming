#!/usr/bin/python3

"""square class

    defining class args
"""


class Square:
    """class square

    defining class args

    """

    def __init__(self, size=0):
        """square has a size

        the size of the square

        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
