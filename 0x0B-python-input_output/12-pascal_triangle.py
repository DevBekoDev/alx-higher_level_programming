#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    class pascal triangle
    """
    rows = []
    for i in range(n):
        row = [1] * (i + 1)
        rows.append(row)
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n - 1][i:i + 2])
    return rows
