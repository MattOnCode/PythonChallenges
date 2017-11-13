import unittest
from .dunthorne import word_valid, get_allowed_words


class TestDunthorne(unittest.TestCase):

    def test_valid_word(self):
        expected_result = True
        actual_result = word_valid("eggs", "aiou")
        self.assertEqual(actual_result, expected_result)

    def test_invalid_word(self):
        expected_result = False
        actual_result = word_valid("apple", "aiou")
        self.assertEqual(actual_result, expected_result)

    def test_allowed_words(self):
        word_list = ["test", "apple", "eggs", "grapes"]
        expected_result = ["test", "eggs"]
        actual_result = get_allowed_words(word_list, "aiou")
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
