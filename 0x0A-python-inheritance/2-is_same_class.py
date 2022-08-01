#!/usr/bin/python3
"""
returns True if object is exactly an instance of
specified class : False if otherwise

"""


def is_same_class(obj, a_class):
    """
    Args: @obj: object
          @a_class: class
    """
    return True if type(obj) == a_class else False
