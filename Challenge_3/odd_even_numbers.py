def odd_even(numbers_list):
    """
    Returns a pair of lists from a list of numbers. One containing odd numbers,
    and the other containing the even numbers.
    :param numbers_list: A list of numbers given by the user.
    :return: The pair of lists (odd and even)
    """
    odd_numbers = []
    even_numbers = []

    for number in numbers_list:
        if number % 2 == 1:
            odd_numbers.append(number)
        else:
            even_numbers.append(number)

    return odd_numbers, even_numbers


def sum_powers(l, p):
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


# Testing the functions
odd, even = odd_even(list(range(20)))

print('Odds: ', odd)
print('Evens:', even)

print('Sum of squared odds', sum_powers(odd, 2))
print('Sum of squared evens', sum_powers(even, 2))
