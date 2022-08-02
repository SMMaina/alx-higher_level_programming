#!/usr/bin/python3
""" fucntion that rets a json string rep of an object """
import json


def to_json_string(my_obj):
    """
    Rets a json rep of sn object (string)
    Args:
        @my_obj : string rep
    """
    return json.dumps(my_obj)
