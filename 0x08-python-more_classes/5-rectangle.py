#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """ Rectangle Class"""

    def __init__(self, width=0, height=0):
        """
        width and height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calcuate the Area of the Rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        calcuate the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter

    def __str__(self):
        """
        Draw the Rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            str = ""
            for row in range(self.__height):
                for col in range(self.__width):
                    str += '#'
                if self.__width != 0 and row < (self.__height - 1):
                    str += '\n'
        return str

    def __repr__(self):
        """
        String represntation for the rectangle
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        print a message when an instance get deleted
        """

        print("Bye rectangle...")
