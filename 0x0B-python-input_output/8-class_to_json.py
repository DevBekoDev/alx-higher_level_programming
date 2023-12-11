#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    """
    return dictionary description of a class
    """

    return obj.__dict__
