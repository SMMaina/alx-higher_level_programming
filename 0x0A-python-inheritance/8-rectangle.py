#!/usr/bin/python3
""" Class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiate with widtha nd height:
        validated by integer_validator
        Args: @width: width
              @height: height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
