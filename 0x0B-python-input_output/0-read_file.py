#!/usr/bin/python3
"""
func to read files
"""


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
