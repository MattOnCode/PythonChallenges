import unittest
from .zipper import zipper


class TestTerms(unittest.TestCase):

    def test_zipper(self):
        first_list = [4, 5, 6, 7, 8, 9, 10]
        second_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        expected_result = [[4, 'A'], [5, 'B'], [6, 'C'], [7, 'D'], [8, 'E'], [9, 'F'], [10, 'G']]
        actual_result = zipper(first_list, second_list)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
