def cumulative(numbers):
    """
    Takes a list of numbers, and generates a cumulative list using the values.
    :param numbers: The list of numbers.
    :return: A new cumulative list of numbers.
    """
    new_list = []
    for number in numbers:
        if numbers.index(number) != 0:
            new_list.append(numbers[numbers.index(number)] + numbers.index(number-1))
    return new_list


# Tests the function.
this_list = list(range(21))
print("Original List: {}".format(this_list))
print("Cumulative List: {}".format(cumulative(this_list)))
