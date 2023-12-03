#!/usr/bin/python3

"""This module contains a function that returns
a list of lists of integers representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """This function returns a list of lists of
    integers representing the Pascal's triangle of n"""
    pascal_triangle = []

    if n <= 0:
        return pascal_triangle
    elif n == 1:
        pascal_triangle.append([1])
    else:
        for i in range(n):
            if i == 0:
                pascal_triangle.append([1])
            elif i == 1:
                pascal_triangle.append([1, 1])
            else:
                pascal_triangle_cpy = []
                for j in range(i):
                    if j == 0:
                        pascal_triangle_cpy.append(pascal_triangle[i-1][j])
                    else:
                        pascal_triangle_cpy.append(pascal_triangle[i-1][j-1]
                                                   + pascal_triangle[i-1][j])
                pascal_triangle_cpy.append(1)
                pascal_triangle.append(pascal_triangle_cpy)
    return pascal_triangle
