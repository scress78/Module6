import unittest
from Module6.more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        """Tests only mandatory arguments"""
        self.assertEqual(score_input("Math Test"), "Math Test: 0.0")

    def test_score_input_test_score_valid(self):
        """Tests mandatory argument plus one known valid second argument"""
        self.assertEqual(score_input("Math Test", 100), "Math Test: 100.0")

    def test_score_input_test_score_below_range(self):
        """Tests mandatory argument plus one known invalid, <0 second argument"""
        self.assertEqual(score_input("Science Test", -10), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self):
        """Tests mandatory argument plus one known invalid, >100 second argument"""
        self.assertEqual(score_input("Physics Test", 212), "Invalid test score, try again!")

    def test_test_score_non_numeric(self):
        """Tests mandatory argument plus one invalid non-numeric argument for error handling"""
        self.assertEqual(score_input("A true test of life..", "...You're still getting there, that's ok"), "This isn't a number. Stop being so philosophical and enter one already.")

    def test_score_input_invalid_message(self):
        """Tests mandatory argument plus, plus invalid second argument, plus optional third argument for custom invalid messages"""
        self.assertEqual(score_input("Banana Test", 120, "Anything but a banana makes no sense. Stop it."), "Anything but a banana makes no sense. Stop it.")


if __name__ == '__main__':
    unittest.main()
