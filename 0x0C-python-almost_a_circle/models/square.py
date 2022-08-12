#!/usr/bin/python3
""" creating a class square that inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square definition """
    def __init__(self, size, x=0, y=0, id=None):
        """ intantialization """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """reps a squae
        [Square] (<id>) <x>/<y> - <size> """
        a = self.id
        b = self.y
        c = self.x
        d = self.size
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(a, c, b, d)

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, side):
        """ setter size """
        self.width = side
        self.height = side
