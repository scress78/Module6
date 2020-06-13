"""
Program: string_functions.py
Author: Spencer Cress
Date: 6/13

Function parameter and return assignment
"""


def multiply_string(message, n):
    """
    This function takes in a message and number and prints the message
    that number of times.
    :param message: the message to be printed
    :param n: number of times message will be printed
    :returns: message printed n number of times
    """
    return message*n


if __name__ == '__main__':
    print(multiply_string("Spencer", 3))
