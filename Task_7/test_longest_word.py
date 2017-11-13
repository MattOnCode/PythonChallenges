import unittest
from .longest_word import longest


class TestDunthorne(unittest.TestCase):

    def test_longest_word_one(self):
        expected_result = "orange"
        actual_result = longest(["red", "blue", "orange", "pink"])
        self.assertEqual(actual_result, expected_result)

    def test_longest_word_two(self):
        expected_result = "potato"
        actual_result = longest(["apple", "grape", "potato"])
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
