"""
Program: inner_functions_assignment.py
Author: Spencer Cress
Date: 6/16

Inner Functions assignment
"""


def measurements(a_list):
    """
    :param a_list: A list of dimensions for a rectangle that will be fed into underlying functions
    :return: with help of other functions returns a message that contains the perimeter and area of said rectangle
    """
    def area(b_list):
        """
        :param b_list: A list of dimensions for a rectangle that will be fed into function
        :return: given the dimensions of a rectangle or square, returns area
        """
        if len(a_list) == 1:
            area_x = a_list[0] ** 2
        if len(a_list) == 2:
            area_x = a_list[0] * a_list[1]
        return area_x

    def perimeter(c_list):
        """
        :param c_list: A list of dimensions for a rectangle that will be fed into function
        :return: given the dimensions of a rectangle or square, returns perimeter
        """
        if len(a_list) == 1:
            perimeter_x = a_list[0] * 4
        if len(a_list) == 2:
            perimeter_x = a_list[0] * 2 + a_list[1] * 2
        return perimeter_x

    return "Perimeter = "+str(perimeter(a_list))+" Area = "+str(area(a_list))

    """def area(area_side_one, area_side_two):
        rec_area = float(area_side_one * area_side_two)
        return rec_area

    def perimeter(perimeter_side_one, perimeter_side_two):
        rec_perimeter = float(perimeter_side_one * 2 + perimeter_side_two * 2)
        return rec_perimeter
    area(*a_list)
    perimeter(*a_list)
    return "Perimeter = "+str(rec_perimeter)+" Area = "+str(rec_area)"""


measurements([2.5, 9])
