#!/usr/bin/python3
""" class Student with attributes:
first_name, last_name, age
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ instantiate with first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dict rep of student instance """
        if attrs is None:
            return self.__dict__
        if all(attrs):
            my_dict = {}
            for i in attrs:
                if i in self.__dict__ and type(i) == str:
                    my_dict[i] = self.__dict__[i]
            return my_dict

    def reload_from_json(self, json):
        """ replaces all attrs of Student instnace """
        for e_key, e_value in json.items():
            self.__dict__[e_key] = e_value
