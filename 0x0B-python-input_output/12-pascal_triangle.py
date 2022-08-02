#!/usr/bin/python3
""" function that retsa list of lists of a pascal triangle """


def pascal_triangle(n):
    """
    returns a list of lists of ints rep Pascals triangle
    Args: @n:
    """
    triangle = []
    if n <= 0:
        return triangle
    elif n == 1:
        triangle.append([1])
        return triangle
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            ilist = [1]
            for b in range(1, i):
                ilist.append(triangle[i - 1][b - 1] +
                             triangle[i - 1][b])
            ilist.append(1)
            triangle.append(ilist)

    return triangle
