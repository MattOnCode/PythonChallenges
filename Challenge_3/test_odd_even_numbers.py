import unittest
from .odd_even_numbers import odd_even, sum_powers


class TestOddEvenNumbers(unittest.TestCase):

    def test_odd_even_numbers_one(self):
        test_passed = False
        expected_result1, expected_result2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        actual_result1, actual_result2 = odd_even(list(range(20)))
        if expected_result1 == actual_result1 and expected_result2 == actual_result2:
            test_passed = True
        self.assertTrue(test_passed)

    def test_odd_even_numbers_two(self):
        test_passed = False
        expected_result1, expected_result2 = [1, 3, 5, 7, 9], [0, 2, 4, 6, 8]
        actual_result1, actual_result2 = odd_even(list(range(10)))
        if expected_result1 == actual_result1 and expected_result2 == actual_result2:
            test_passed = True
        self.assertTrue(test_passed)

    def test_odd_even_numbers_three(self):
        test_passed = False
        expected_result1, expected_result2 = [1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10, 12]
        actual_result1, actual_result2 = odd_even(list(range(13)))
        if expected_result1 == actual_result1 and expected_result2 == actual_result2:
            test_passed = True
        self.assertTrue(test_passed)

    def test_odd_even_numbers_squared(self):
        test_passed = False
        expected_result1, expected_result2 = 286, 364
        odd_numbers, even_numbers = odd_even(list(range(13)))
        actual_result1, actual_result2 = sum_powers(odd_numbers, 2), sum_powers(even_numbers, 2)
        if actual_result1 == expected_result1 and actual_result2 == expected_result2:
            test_passed = True
        self.assertTrue(test_passed)


if __name__ == '__main__':
    unittest.main()
