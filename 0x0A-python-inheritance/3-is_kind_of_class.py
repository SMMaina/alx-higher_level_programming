#!/usr/bin/python3
"""
function that returns True if object is an intance of,
or if the object is na intance of class its inherited from
otherwise False

"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        @obj: object
        @a_class: class
    """
    return isinstance(obj, a_class)
         
