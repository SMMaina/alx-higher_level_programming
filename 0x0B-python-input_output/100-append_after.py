#!/usr/bin/python3
""" fucntion that inserts line to text file after
each line containing a spec string """


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    Args:
        @filename: name of file
        @search_string: searched str in file
        @new_string: new string to add after search_string
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        stringline = ""
        for i in file:
            stringline += i
            if search_string in i:
                stringline += new_string
        file.seek(0)
        file.write(stringline)
