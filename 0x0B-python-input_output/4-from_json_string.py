#!/usr/bin/python3
""" function that converts json string to string """
import json


def from_json_string(my_str):
    """
    Returns to JSON rep of an object(string)
    Args:
        @my_str:
    """
    return json.loads(my_str)
