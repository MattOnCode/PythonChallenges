"""
Challenge:
Create a function longest(words) to find the longest word in a list of strings.
"""


def longest(words):
    """
    Finds the longest word in a list of words.
    :param words: A list of words (strings).
    :return: The longest word from the list.
    """
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


# Testing the function
list_of_words = ["pie", "chips", "apple", "potato", "carrot", "orange"]

print(longest(list_of_words))
