#!/usr/bin/python3
"""
fucntion that returns True if object is an instance
of class that inherited (directly or indirectly) fro the 
class ; False if otherwise

"""


def inherits_from(obj, a_class):
    """
    Args: @obj: object
          @a_class: class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
