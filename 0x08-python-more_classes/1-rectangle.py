#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new rectnagle.
        Args:
            height (int): The height of the new rectangle.
            Width (int): The width of the new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Set the width of the new retangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """Set the height of the new rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
