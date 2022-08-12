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

    def update(self, *args, **kwargs):
        """ assigns a n arg to each attribute without need of a key word """
        if len(args) > 0:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                elif n == 1:
                    super(Square, type(self)).width.fset(self, arg)
                    super(Square, type(self)).height.fset(self, arg)
                elif n == 2:
                    super(Square, type(self)).x.fset(self, arg)
                elif n == 3:
                    super(Square, type(self)).y.fset(self, arg)
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                super(Square, type(self)).width.fset(self, kwargs["size"])
                super(Square, type(self)).height.fset(self, kwargs["size"])
            if "x" in kwargs:
                super(Square, type(self)).x.fset(self, kwargs["x"])
            if "y" in kwargs:
                super(Square, type(self)).y.fset(self, kwargs["y"])

    def to_dictionary(self):
        """ conversion of class square to dict """
        myid = self.id
        x = super().x
        y = super().y
        w = super().width
        return {'x': x, 'y': y, 'id': myid, 'size': w}
