#!/usr/bin/python3
""" Class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        instantiate size:
        validated by integer_validator
        Args: @size: size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        area method
        Args: @self: size
        """
        return self.__size ** 2

    def __str__(self):
        """
        str module to ret a class rep
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

