import unittest
from .cumulative import cumulative


class TestTerms(unittest.TestCase):

    def test_cumulative(self):
        number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_result = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        actual_result = cumulative(number_list)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
