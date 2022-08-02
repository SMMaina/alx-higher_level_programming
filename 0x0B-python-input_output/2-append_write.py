#!/usr/bin/python3
""" appanes a string to a text file """


def append_write(filename="", text=""):
    """
    Returns number of chars added
    Args:
        @filename: name of file to open from nain
        @numlines: number of lines to read
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
