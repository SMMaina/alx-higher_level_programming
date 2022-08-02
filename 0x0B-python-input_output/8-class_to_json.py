#!/usr/bin/python3
"""
function that resturns a dict rep with simple data structure
returns a serialized object
"""


def class_to_json(obj):
    """
    rets the dict decription
    Args: @obj: object
    """
    return obj.__dict__
