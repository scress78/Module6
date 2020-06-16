"""
Program: validate_input_in_functions.py
Author: Spencer Cress
Date: 6/16
Function Default Values Assignment
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: Name of the test, a string
    :param test_score: Score for the Test, a float or integer
    :param invalid_message: Message given when invalid input is entered
    :return: Returns test name and score, given valid input
    """
    valid_input = 0
    try:
        test_score = float(test_score)
    except ValueError:
        valid_input = "This isn't a number. Stop being so philosophical and enter one already."
    else:
        valid_input = test_name+": "+str(test_score)
        if test_score < 0:
            valid_input = invalid_message
        if test_score > 100:
            valid_input = invalid_message
    return valid_input


if __name__ == '__main__':
    score_input("Math Test", "I'm too macho for math, nerd")


