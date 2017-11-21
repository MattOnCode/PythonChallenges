import unittest
from .word_count import word_count


class TestTerms(unittest.TestCase):

    def test_word_count_one(self):
        test_passed = False
        word_list = ['This', 'is', 'an', 'amazing', 'list', 'of', 'words']
        expected_word_count, expected_letter_count = 7, 26
        actual_word_count, actual_letter_count = word_count(word_list)
        if expected_word_count == actual_word_count and expected_letter_count == actual_letter_count:
            test_passed = True
        self.assertTrue(test_passed)

    def test_word_count_two(self):
        test_passed = False
        word_list = ['Big', 'giant', 'alphabetical', 'fuel', 'consumption', 'warnings']
        expected_word_count, expected_letter_count = 6, 43
        actual_word_count, actual_letter_count = word_count(word_list)
        if expected_word_count == actual_word_count and expected_letter_count == actual_letter_count:
            test_passed = True
        self.assertTrue(test_passed)


if __name__ == '__main__':
    unittest.main()
