#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Reps a rectangle.
    Attributes:
        number_of_instances (int): the number of rectangle instances
        print_symbol (any): the symbol used for st rep
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the Rectangle."""
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
        """Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the printable rep of the rectangle
        Reps the rectangle with the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return the string rep of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print message for every deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

