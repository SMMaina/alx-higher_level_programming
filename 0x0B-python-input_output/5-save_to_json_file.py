#!/usr/bin/python3
""" function that writes to a textfile using json rep """
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    Args:
        @my_obj: object
        @filename: name of file to write or create
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
