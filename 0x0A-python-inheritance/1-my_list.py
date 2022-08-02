#!/usr/bin/python3
"""
class MyList from list:

def print_sorted(self): method that prints the list, but sorted(ascending order.
"""


class MyList(list):
    """
    Args: list from parent list
    """

    def print_sorted(self):
        """
        public instance method that prints the list
        in sorted (ascending order)
        Args: @self: inherits output from parent
        """
        print(sorted(self))
