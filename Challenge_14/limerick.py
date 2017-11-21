limerick = [
    ['There','was', 'a', 'young', 'lady', 'named', 'Wright'],
    ['Whose', 'speed', 'was', 'much', 'faster', 'than', 'light'],
    ['She', 'left', 'home', 'one', 'day'],
    ['In', 'a', 'relative', 'way'],
    ['And', 'returned', 'on', 'the', 'previous', 'night']
]


def print_limerick(word_list):
    """
    Outputs the contents of a multidimensional list.
    :param word_list: The multidimensional list.
    :return: Does not return data.
    """
    for list in word_list:
        for word in list:
            print(word, end=' ')


def count_limerick(word_list):
    """
    Counts the amount of words, and letters, in a multidimensional list.
    :param word_list: The multidimensional list.
    :return: The count of words, and letters, within the list.
    """
    sum_words = 0
    sum_letters = 0
    for list in word_list:
        for word in list:
            sum_words += 1
            for letter in word:
                sum_letters += 1
    return sum_words, sum_letters


# Testing the functions
words, letters = count_limerick(limerick)
print_limerick(limerick)
print("\nTotal words: {}\nTotal letters: {}".format(words, letters))
