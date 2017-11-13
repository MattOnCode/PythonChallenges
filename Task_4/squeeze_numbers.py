"""
Challenge:
Create function squeeze(numbers_list) that takes a list and returns the list where all
adjacent elements that are the same have been reduced to a single element.
"""


def squeeze(numbers_list):
    squeezed_list = []
    for number in numbers_list:
        if number not in squeezed_list:
            squeezed_list.append(number)
    return squeezed_list


# Testing the functions
for number_list in [[1, 2, 2, 3, 3, 4], [1, 2, 3, 4], [3, 3, 3, 3, 3, 3], [3], []]:
    print(number_list, "squeezed is", squeeze(number_list))
