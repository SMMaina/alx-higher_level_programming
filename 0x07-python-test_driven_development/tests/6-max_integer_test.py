#!/usr/bin/python3
"""
   Unit test module for max_integer function
   Class:
       TestMaxInteger(unittest.Testcase)
       Methods:
           tests_max_integer
"""
import unittest


class TestMaxInteger(unittest.TestCase):
    """
       TestCase Subclass
       Use: testing max_integer fucntion in 6-max_integer
    """
    max_integer = __import__('6-max_integer').max_integer

    def test_max_integer(self):
        """
           Test method for right answer
           Test cases: no list, ascedning, descending,
                          random, more than one max value
        """
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertAlmostEqual(max_integer([1, 5, 0, 5]), 5)
        self.assertAlmostEqual(max_integer([1, 9, 3, 7]), 9)

    def test_max_integer_raises(self):
        """
            Test method for errors rasies
            Test cases: non list data types, list with none integer data types,
                        list with mixed data types
        """
        self.assertRaises(TypeError, max_integer("hello"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertRaises(TypeError, max_integer(["hello", "hi"]))
        with self.assertRaises(TypeError):
            max_integer([1, "hello"])
        with self.asertRaises(TypeError):
            max_integer(1)
