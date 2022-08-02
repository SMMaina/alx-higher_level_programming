#!/usr/bin/python3
""" function that creates an object from a json file """
import json


def load_from_json_file(filename):
    """
    Args:
        @filename : name of file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
