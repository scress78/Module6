import unittest
from Module6.Topic4.Function_Default_Values import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input("Math Test"), "Math Test: 0")

    def test_score_input_test_valid(self):
        self.assertEqual(score_input("Math Test", 100), "Math Test: 100")
    #assert score_input("ScienceTest", -10) == "Invalid test score, try again!"
    #def test_above_range(self):
        #assert score_input("Physics Test", 10000) == "Invalid test score, try again!"
    #def test_nonnumeric(self):
        #assert score_input("A True Test of Life", "...Well, you're still working on it :)") == ValueError


if __name__ == '__main__':
    unittest.main()
