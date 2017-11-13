"""
Challenge:
Create function odd(numbers_list) that takes a list of numbers and returns a list of the odd numbers.
"""


def odd(numbers_list):
    """
    Returns the odd numbers from the given list in a list.
    :param numbers_list: A list of numbers given by the user.
    :return: A list containing the odd numbers.
    """
    odd_numbers = []

    for number in numbers_list:
        if number % 2 == 1:
            odd_numbers.append(number)

    return odd_numbers


# Testing the function
print("List of odd numbers: {}".format(odd(list(range(35)))))
