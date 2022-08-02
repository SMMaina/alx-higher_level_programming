#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nbchar = write_file("myfile.py", "this is so cool\n")
print(nbchar)
