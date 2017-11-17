rhyme = ['Mary', 'had', 'a', 'little', 'lamb', 'whose', 'fleece', 'was', 'white', 'as', 'snow']


def word_count(L):
    """
    Counts the amount of words, and letters, within the given list.
    :param L: The list of words.
    :return: Integer pair of the amount of letters, and the amount of words.
    """
    sum_words = 0
    sum_letters = 0
    for word in L:
        sum_words += 1
        for letter in word:
            sum_letters += 1

    return sum_words, sum_letters


# Tests the function.
letters, words = word_count(rhyme)
print("Amount of words in list: {}".format(words))
print("Amount of letters in list: {}".format(letters))
