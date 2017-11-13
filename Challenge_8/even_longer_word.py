import os.path

# Friendly path to file of words.
project_path = os.path.dirname(__file__)
word_file = os.path.join(project_path, 'words.txt')


def all_longest(words):
    """
    Finds the longest word in a list of words.
    :param words: A list of words (strings).
    :return: The longest word from the list.
    """
    longest_word = ""
    list_longest_words = []

    # Finds the longest word.
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # Adds all words of the longest words length to the list.
    for word in words:
        if len(word) == len(longest_word):
            list_longest_words.append(word)

    return list_longest_words


words = []
for line in open(word_file, 'r').readlines():
    words.append(line.strip().lower())

print(all_longest(words))
