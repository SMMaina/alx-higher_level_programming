#!/usr/bin/python3
""" class Student that also retrieves itsel
with public attributes:
first_name, last_name, age
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """instantiate class with first_name, last_name, and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary rep of student """
        if attrs is None:
            return self.__dict__
        if all(attrs):
            my_dict = {}
            for i in attrs:
                if i in self.__dict__ and type(i) == str:
                    my_dict[i] = self.__dict__[i]
            return my_dict
