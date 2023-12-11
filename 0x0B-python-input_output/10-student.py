#!/usr/bin/python3
"""
class Student
"""


class Student:
    """
    class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        define public instances atributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a dictionary representation of a Student instance
        """

        if attrs is not None:
            dic = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return dic
        else:
            return self.__dict__
