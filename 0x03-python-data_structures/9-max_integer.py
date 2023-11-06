#!/usr/bin/python3
def max_integer(my_list=[]):
    s = 0
    if len(my_list) <= 0:
        s = None
        return s
    for i in range(len(my_list)):
        if my_list[i] >= s:
            s = my_list[i]
    return s

