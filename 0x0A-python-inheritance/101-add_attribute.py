#!/usr/bin/python3
""" adds a new attribute to an object if possible """


def add_attribute(obj, key, value):
    """
    set attribute
    Args:
        @obj: object
        @key: key
        @value: value
    Arguments are a object and a  string
    return True is string is name of class object attrbutes ofr False
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
