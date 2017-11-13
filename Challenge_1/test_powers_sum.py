import unittest
from .powers_sum import sum_powers


class TestPowersSum(unittest.TestCase):

    def test_sum_powers_one(self):
        expected_result = 285
        actual_result = sum_powers(list(range(10)), 2)
        self.assertEqual(actual_result, expected_result)

    def test_sum_powers_two(self):
        expected_result = 120825
        actual_result = sum_powers(list(range(10)), 5)
        self.assertEqual(actual_result, expected_result)

    def test_sum_powers_three(self):
        expected_result = 4914341925
        actual_result = sum_powers(list(range(10)), 10)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
