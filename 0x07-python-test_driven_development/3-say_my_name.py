#!/usr/bin/python3
"""
    printing module
    Functions:
        say_my_name(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """
        Function that prints names
        Args:
            first_name: fisrt name
            last_name: last name
        Return: nothing
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("{:s} {:s}".format(first_name, last_name))
