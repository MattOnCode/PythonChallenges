import unittest
from .odd_numbers import odd


class TestOddNumbers(unittest.TestCase):

    def test_odd_numbers_one(self):
        expected_result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        actual_result = odd(list(range(20)))
        self.assertEqual(actual_result, expected_result)

    def test_odd_numbers_two(self):
        expected_result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
        actual_result = odd(list(range(40)))
        self.assertEqual(actual_result, expected_result)

    def test_odd_numbers_three(self):
        expected_result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
        actual_result = odd(list(range(35)))
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
