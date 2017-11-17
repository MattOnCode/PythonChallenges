import unittest
from .palidrome import palindrome


class TestTerms(unittest.TestCase):

    def test_palindrome(self):
        word_list = ['Apple', 'Wow', 'Cellphone', 'Amazing', 'Yay']
        expected_result = ['Wow', 'Yay']
        actual_result = palindrome(word_list)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
