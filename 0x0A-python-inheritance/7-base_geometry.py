#!/usr/bin/python3
"""
Class Basegeometry

"""


class BaseGeometry:
    """
    Class BaseGeometry
    """

    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemenetd")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
