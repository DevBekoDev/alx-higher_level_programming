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

    def __init__(self, size=0, position=(0, 0)):
        """square has a size

        the size of the square

        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if not(isinstance(position, tuple) and
                len(position) == 2 and isinstance(position[0], int) and
                isinstance(position[1], int) and position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def position(self):
        """posiiton
        private
        """
        return self.__position

    @position.setter
    def position(self, value):
        """the value of position

        value
        """

        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[1], int) and isinstance(value[0], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area of a square

        area = size ** 2
        """

        return (self.__size ** 2)

    def my_print(self):
        """print the square

        in form of #
        """
        if self.__size == 0:
            print("")
        else:
            for x in range(0, self.__position[1]):
                print()
            for x in range(0, self.__size):
                print((" " * self.__position[0]) + "#" * self.__size)
