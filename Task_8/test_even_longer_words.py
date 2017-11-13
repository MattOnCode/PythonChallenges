import unittest
from .even_longer_word import longest


class TestDunthorne(unittest.TestCase):

    def test_longest_words_one(self):
        expected_result = ["potato", "carrot", "orange"]
        actual_result = longest(["potato", "carrot", "blue", "orange"])
        self.assertEqual(actual_result, expected_result)

    def test_longest_words_two(self):
        expected_result = ["could", "jesus"]
        actual_result = longest(["red", "bed", "sad", "fled", "could", "yes", "jesus"])
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
