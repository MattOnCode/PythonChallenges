import os.path

# Friendly path to file of words.
word_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'words.txt'))


def palindrome(words):
    """
    Finds all the palindromes within the given list of words.
    :param words: The list of words.
    :return: A new list containing the palindromes.
    """
    palindromes = []
    for word in words:
        if word[::-1].lower() == word.lower():
            palindromes.append(word)
    return palindromes


# Creates list of words from file excluding white spacing
file_words = []
for line in open(word_file, 'r').readlines():
    file_words.append(line.strip().lower())

# Prints out all the palindromes
file_palindromes = palindrome(file_words)
for word in file_palindromes:
    print(word)
