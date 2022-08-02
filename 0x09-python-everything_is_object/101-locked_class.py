#!/usr/bin/python3
"""
low memory cost: class which is locked and contains no class or object
it prevents the suer from dynamically creating new instance
except first intance is called first_name
"""


class LockedClass():
    """
    prevents the suer from dynamically creating new instance
    """

    __slots__ = ['first_name']
