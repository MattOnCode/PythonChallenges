import re
import unittest

numbers = []


def validate_input(user_input):
    """
    Validates whether the input is a number, or whether it is Q or q
    which will finish the application.
    :param user_input: The users inputted value.
    :return: True/False dependent on whether it is Q/q or not.
    """
    return False if re.search("[Qq]", user_input) else True


def calculate_average(number_list):
    """
    Calculates the average of all the numbers within a list.
    :param number_list: The list of numbers.
    :return: The average of the numbers.
    """
    numbers_sum = 0
    for number in number_list:
        numbers_sum += number
    return numbers_sum / len(number_list)


while True:
    input_number = input("Enter a number: ")
    if validate_input(input_number):
        numbers.append(int(input_number))
    else:
        print("Average: {}".format(calculate_average(numbers)))
        break