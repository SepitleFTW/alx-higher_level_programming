#!/usr/bin/python3
"""defines pascals tri function"""


def pascals_triangle(n):
    """represents truangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
