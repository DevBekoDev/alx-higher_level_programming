#!/usr/bin/python3
"""
I/O python
"""


def read_file(filename=""):
    """
    func to read a file
    """

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
