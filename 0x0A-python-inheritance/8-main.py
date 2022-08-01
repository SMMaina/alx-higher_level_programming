#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 7)

print(r)
print(dir(r))

try:
    print(r.width, r.height)
except Exception as e:
    print(e.__class__.__name__, e)
