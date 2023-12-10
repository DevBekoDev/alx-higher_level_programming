#!/usr/bin/python3
"""
write to a file
"""


def write_file(filename="", text=""):
    """
    write the text into a file
    with specified filename
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
