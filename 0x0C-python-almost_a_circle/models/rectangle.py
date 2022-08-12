#!/usr/bin/python3
""" craeting a calass recangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class initialzer """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of Rectangle instance. """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout rectangle instance iwth # """
        for y in range(self.__y):
            print()
        for v in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ rectruns a customized strig version """
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__height
        e = self.__width
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(a, b, c, e, d)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute in a specific order """
        if len(args) > 0:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ conversion of class to dictionary """
        myid = self.id
        x = self.__x
        y = self.__y
        h = self.__height
        w = self.__width
        return {'x': x, 'y': y, 'id': myid, 'height': h, 'width': w}
