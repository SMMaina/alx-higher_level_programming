#!/usr/bin/python3
""" script that adds all rgs to a python list and saves it """
from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"

new_list = []

if not path.exists(file):
    save_to_json_file(new_list, file)

new_list = list(load_from_json_file(file))

for index in argv[1:]:
    new_list.append(index)

save_to_json_file(new_list, file)
