import unittest
from Module6.Topic4.Function_Default_Values import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input("Math Test"), "Math Test: 0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input("Math Test", 100), "Math Test: 100")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input("Science Test", -10), "Invalid test score, try again!")

    #def test_score_input_test_score_above_range(self):
        #self.assertEqual(score_input("Physics Test", 212), "Invalid test score, try again!")

    #def test_test_score_non_numeric(self):
        #self.assertRaises(score_input("A true test of life..", "...You're still getting there, that's ok"), ValueError)


if __name__ == '__main__':
    unittest.main()
