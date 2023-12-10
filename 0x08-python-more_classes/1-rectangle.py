#!/usr/bin/python3
"""
Rectangle Class
"""


class Rectangle:
    """ Rectangle Class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @setter.width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    @property
    def height(self):
        return self.height

    @setter.height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = value

