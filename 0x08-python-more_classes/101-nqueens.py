#!/usr/bin/python3
"""
    Nqueens module(Chess)
"""
import sys


def is_exist(y):
    """ Method that dets a queen doe not aleady exist in the y val
    Args:
        y: array tht has queen pos
        nqueen: number
    Returns:
        bool
    """
    for m in range(num):
        if queens[m][1] == y:
            return True
    return False


def refuse(x, y):
    """ funct that checks queen pos
    Args:
        x (int): queen number
        y (int): pos index
    Returns: bool
    """
    if (is_exist(y)):
        return False
    i = 0
    while (i < x):
        if abs(queens[i][1] - y) == abs(i - x):
            return False
        i += 1
        return True


def solveN(x):
    """ recursive funct that solves the backtracking algorithm
    Args:
        x: queen num
    """
    for y in range(num):
        for i in range(x, num):
            queens[i][1] = -1
        if refuse(x, y):
            queens[x][1] = y
            if (x == num - 1):
                print(queens)
            else:
                solveN(x + 1)


if __name__ == "__main__":
    """
        programs entry point
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    else:
        if num < 4:
            print("N must be atleast 4")
            exit(1)
        else:
            queens = [[i, -1] for i in range(num)]
            solveN(0)

