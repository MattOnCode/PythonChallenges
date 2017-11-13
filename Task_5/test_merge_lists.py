import unittest
from .merge_lists import merge


class TestOddNumbers(unittest.TestCase):

    def test_merge_lists_one(self):
        expected_result = [1, 2, 3, 4, 5, 6]
        actual_result = merge([1, 2, 6], [3, 4, 5])
        self.assertEqual(actual_result, expected_result)

    def test_merge_lists_two(self):
        expected_result = [10, 14, 16, 17, 18, 20]
        actual_result = merge([14, 17, 20], [10, 16, 18])
        self.assertEqual(actual_result, expected_result)

    def test_merge_lists_three(self):
        expected_result = [22, 34, 42, 45, 46, 50]
        actual_result = merge([42, 46, 50], [22, 34, 45])
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
