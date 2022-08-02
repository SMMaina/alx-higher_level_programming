#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

mylist = "[1, 2, 3]"
stringlist = from_json_string(mylist)
print(stringlist)
print(type(stringlist))
