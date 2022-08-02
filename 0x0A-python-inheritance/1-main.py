#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class myclass1(object):
    pass

class myclass2(object):
    myattr = 3
    def mymethod(self):
        pass

print(lookup(myclass1))
print(lookup(myclass2))
print(lookup(int))
