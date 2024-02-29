#!/usr/bin/python3
""" find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(ini): list of integers to find peak from
    Returns:
            peak of list_of_integers or None
    """
    size = len(list_of_integers)
    if size == 0:
        return None
    left = 0
    right = size - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
