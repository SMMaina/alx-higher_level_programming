#!/usr/bin/python3
"""
defining a class student with attributes firstname, lastname and age
with a method that serializes it.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ instantiate with first_name, last_name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ restrieves a dictionary rep """
        return self.__dict__
