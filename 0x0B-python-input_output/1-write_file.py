#!/usr/bin/python3
""" function that retyurns no of lines of a text file written """


def write_file(filename="", text=""):
    """
    Args:
        @filename: name of fle to open from main
        @numlines: number of lines to read from file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
