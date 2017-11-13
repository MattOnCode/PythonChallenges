import unittest
from .terms import sum_powers, terms


class TestTerms(unittest.TestCase):

    def test_sum_powers(self):
        expected_result = 225
        actual_result = sum_powers(5, 3)
        self.assertEqual(actual_result, expected_result)

    def test_terms(self):
        expected_result = 14
        actual_result = terms(10000, 3)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
