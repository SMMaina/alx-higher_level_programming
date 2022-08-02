#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "susan")
print(mc.name)

try:
    a = "my sock"
    add_attribute(a, "name", "sus")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
