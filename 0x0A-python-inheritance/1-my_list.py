#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """ sorted list"""

    pass

    def print_sorted(self):
        """ print the list in sorted form"""

        print(sorted(list(self)))
