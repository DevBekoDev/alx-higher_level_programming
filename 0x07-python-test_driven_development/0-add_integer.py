#!/bin/usr/python3

def add_integer(a, b=98):
    if isinstance(a, int) == False and isinstance(a, float) == False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) == False and isinstance(b, float) == False:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return(a + b)
