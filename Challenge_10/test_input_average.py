import unittest
from .input_average import validate_input, calculate_average


class TestTerms(unittest.TestCase):

    def test_validate_input_false(self):
        expected_result = False
        actual_result = validate_input("q")
        self.assertEqual(actual_result, expected_result)

    def test_validate_input_true(self):
        expected_result = True
        actual_result = validate_input("4")
        self.assertEqual(actual_result, expected_result)

    def test_calculate_average_one(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_result = 5.0
        actual_result = calculate_average(number_list)
        self.assertEqual(actual_result, expected_result)

    def test_calculate_average_two(self):
        number_list = [15, 6, 13, 28, 34, 1, 30, 41]
        expected_result = 21
        actual_result = calculate_average(number_list)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
