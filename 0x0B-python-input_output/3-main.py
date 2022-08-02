#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
jsonlist = to_json_string(my_list)
print(jsonlist)
print(type(jsonlist))
