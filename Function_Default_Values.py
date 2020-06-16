"""
Program: function_default_values.py
Author: Spencer Cress
Date: 6/13
Function Default Values Assignment
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: Name of the test
    :param test_score: Score for the Test
    :param invalid_message: Validates test score
    :return: Returns test name and score
    """
    #test_name = input("Input name of test: ")
    #test_score = input("input score test: ")

    """try:
        test_score = int(test_score)
    except:
        print("Invalid Score")
        raise ValueError"""
    valid_input = 0
    try:
        test_score = float(test_score)
    except ValueError:
        valid_input = "this isn't a number, please enter one"
    else:
        valid_input = test_name+": "+str(test_score)
        if test_score < 0:
            valid_input = invalid_message
        if test_score > 100:
            valid_input = invalid_message
        # else:
            # valid_input = test_name+": "+str(test_score)
    return valid_input


if __name__ == '__main__':
    score_input("Math Test", "machoman")


