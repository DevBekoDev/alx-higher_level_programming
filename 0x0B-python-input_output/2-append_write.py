#!/usr/bin/python3
"""
write to a file
"""


def append_write(filename="", text=""):
    """
    append text to a file
    with the specified filename
    """

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
