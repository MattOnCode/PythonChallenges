def sum_powers(n, p):
    """
    Finds the sum of the first n natural numbers raised to the pth power
    :param n: The amount of numbers
    :param p: The p-th power.
    :return: The sum of the first n natural numbers raised to the pth power
    """
    powers_sum = 0

    for i in range(1, n+1):
        powers_sum += i**p

    return powers_sum


def terms(big, p):
    """
    Returns the number of terms (that is, n) that are needed for the sum of powers to be larger than big.
    :param big: The limit of sum of powers.
    :param p: The p-th power.
    :return: The number of terms needed to be larger than big.
    """
    number_of_terms = 1

    while sum_powers(number_of_terms, p) <= big:
        number_of_terms += 1

    return number_of_terms


print("Number of terms for sum to exceed {} is {}".format(100, terms(100, 3)))
