#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

numchar = append_write("myfile.py", "this is so cool\n")
print(numchar)
