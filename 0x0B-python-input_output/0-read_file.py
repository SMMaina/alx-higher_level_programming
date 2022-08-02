#!/usr/bin/python3
""" fucntion that reads a text file (UTF8) and prints to STDOUT """


def read_file(filename=""):
    """
    read_file(filename=""):
    args: @filename: name of file to open
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
