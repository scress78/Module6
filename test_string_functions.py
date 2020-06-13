import unittest
from Module6.more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual("Spencer", 3, "SpencerSpencerSpencer")


if __name__ == '__main__':
    unittest.main()
