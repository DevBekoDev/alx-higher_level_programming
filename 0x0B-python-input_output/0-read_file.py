#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="UTF8") as f:
        read = f.read()
        return read
