#!/usr/bin/python3
"""
Lookup: function that returns the available list of attributes in a class object

"""


def lookup(obj):
    """
    Args: obj
    Returns a list object
    """
    return dir(obj)
