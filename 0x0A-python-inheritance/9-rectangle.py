#!/usr/bin/python3
""" Class BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class BaseGeometry
    """

    def __init__(self, width, height):
        """
        instantiate with width and height:
        validated by integer_validator
        Args: @width: width
              @height: height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Implement area module
        Return area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        string module ret a class rep
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
