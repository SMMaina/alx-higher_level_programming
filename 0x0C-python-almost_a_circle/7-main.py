#!/usr/bin/python3
""" 7-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)
