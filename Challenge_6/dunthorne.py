import os.path

# Friendly path to file of words.
word_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'words.txt'))

def word_valid(word, string):
    """
    Checks whether or not the given word contains any
    of the characters within the string.
    :param word: The word to validate.
    :param string: The characters to check (in string form)
    :return: True/False depending upon whether it's valid or not.
    """
    for char in string:
        if char in word:
            return False
    return True


def get_allowed_words(words, forbidden="aiou"):
    """
    Gets the allowed words from a list of words, which do not
    contain the forbidden characters.
    :param words: The list of words to check.
    :param forbidden: The forbidden characters (in string form.
    :return: A list of allowed words.
    """
    allowed_words = []
    for word in words:
        if word_valid(word, forbidden):
            allowed_words.append(word)
    return allowed_words


# Gets the words from the file.
words = []
for line in open(word_file, 'r').readlines():
    words.append(line.strip().lower())

# Gets the allowed words.
allowed = get_allowed_words(words)

# Tests the program.
print('There are', len(allowed), 'words not containing aiou')
