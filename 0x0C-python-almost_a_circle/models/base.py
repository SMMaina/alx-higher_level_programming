#!/usr/bin/python3
""" creating a base class """
import json
import os
import csv


class Base:
    """ The goal is to managfe id attribute in al future classes
    to avoid duplication
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ method initializer of the base module. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """ conversion fo dicts to json strings """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Conversion from string to dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json rep of list_objs to a file """
        if list_objs is None or list_objs == []:
            li = []
        else:
            li = [n.to_dictionary() for n in list_objs]
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(li))

    @classmethod
    def create(cls, **dictionary):
        """ rets a n instnace with all attributes set """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        else:
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ returns a list of instanes """
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except:
            return []

        li = []
        with open(str(cls.__name__) + ".json", "r") as f:
            li = cls.from_json_string(f.read())

        instances = len(li)
        inst = []
        for t in range(instances):
            inst.append(cls.create(**li[t]))

        return inst

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV """
        try:
            f = open(str(cls.__name__) + ".csv")
            f.close()
        except:
            return []
        square = ['id', 'size', 'x', 'y']
        rect = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle":
            fieldname = rect
        else:
            fieldname = square

        instance = []
        with open(str(cls.__name__) + ".csv", "r") as fn:
            cd = csv.reader(fn, delimiter=',')
            for n, dictr in enumerate(cd):
                if n > 0:
                    ins = cls(1, 1)
                    for x, y in enumerate(dictr):
                        if y:
                            setattr(ins, fieldname[x], int(y))
                    instance.append(ins)
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the json rep of list_objs """
        if list_objs is None or list_objs == []:
            li = []
        with open(cls.__name__ + ".csv", "w") as fn:
            list_objs = [i.to_dictionary() for i in list_objs]
            rect = ['id', 'width', 'height', 'x', 'y']
            square = ['id', 'size', 'x', 'y']
            if cls.__name__ == "Rectangle":
                f_csv = csv.DictWriter(fn, fieldnames=rect)
            else:
                f_csv = csv.DictWriter(fn, fieldnames=square)
            f_csv.writeheader()
            f_csv.writerows(list_objs)
