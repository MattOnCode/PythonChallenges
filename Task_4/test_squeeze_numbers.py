import unittest
from .squeeze_numbers import squeeze


class TestOddNumbers(unittest.TestCase):

    def test_squeeze_numbers_one(self):
        expected_result1 = [1, 2, 3, 4, 5, 6]
        actual_result1 = squeeze([1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 6])
        self.assertEqual(actual_result1, expected_result1)

    def test_squeeze_numbers_two(self):
        expected_result1 = [9, 6, 7, 8, 3]
        actual_result1 = squeeze([9, 9, 6, 7, 8, 8, 3, 3])
        self.assertEqual(actual_result1, expected_result1)

    def test_squeeze_numbers_three(self):
        expected_result1 = [9, 4, 5, 2, 3]
        actual_result1 = squeeze([9, 9, 9, 4, 9, 5, 5, 2, 3, 4])
        self.assertEqual(actual_result1, expected_result1)


if __name__ == '__main__':
    unittest.main()
