#!/usr/bin/python3
""" 11-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 3, 4, 5)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))
