#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
