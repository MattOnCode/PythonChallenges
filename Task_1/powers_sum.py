"""
Challenge:
Create function sumpowers(l, p=1) that takes a list of numbers and returns the sum of each
number in the list raised to the pth power.
"""


def sum_powers(l, p=1):
    """
    Return the sum of the numbers in L raised to the p-th power.
    :param l: The list of numbers.
    :param p: The p-th power.
    :return: The sum of numbers in L raised to the p-th power.
    """
    powers_sum = 0

    for n in l:
        powers_sum += n**p

    return powers_sum


# Testing the function
for power in range(11):
    result = sum_powers(list(range(10)), power)
    print(power, result)
