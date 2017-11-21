import unittest
from .limerick import count_limerick


class TestTerms(unittest.TestCase):

    def test_count_limerick(self):
        test_passed = False
        test_list = [
            ['This', 'is', 'an', 'example', 'of', 'a', 'multidimensional'],
            ['array', 'and', 'this', 'test', 'proves', 'the', 'function'],
            ['works', 'perfectly'],
        ]
        expected_result_words, expected_result_letters = 16, 81
        actual_result_words, actual_result_letters = count_limerick(test_list)
        if expected_result_words == actual_result_words and expected_result_words == actual_result_words:
            test_passed = True
        self.assertTrue(test_passed)


if __name__ == '__main__':
    unittest.main()
