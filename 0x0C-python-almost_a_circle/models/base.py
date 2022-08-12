#!/usr/bin/python3
""" creating a base class """
import json
import os
import csv


class Base:
    """ The goal is to managfe id attribute in al future classes
    to avoid duplication
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ method initializer of the base module. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """ conversion fo dicts to json strings """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Conversion from string to dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)
