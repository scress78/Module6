"""
Program: test_string_functions.py
Author: Spencer Cress
Date: 6/13

Test the function for parameter and return assignment
"""

import unittest
from Module6.more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        assert multiply_string("Spencer", 3) == "SpencerSpencerSpencer"


if __name__ == '__main__':
    unittest.main()
