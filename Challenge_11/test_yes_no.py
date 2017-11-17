import unittest
from .yes_no import yesno


class TestTerms(unittest.TestCase):

    def test_yesno_Y(self):
        expected_result = False
        actual_result = yesno("Y")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_y(self):
        expected_result = False
        actual_result = yesno("y")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_YES(self):
        expected_result = False
        actual_result = yesno("YES")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_yes(self):
        expected_result = False
        actual_result = yesno("yes")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_n(self):
        expected_result = False
        actual_result = yesno("n")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_N(self):
        expected_result = False
        actual_result = yesno("N")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_no(self):
        expected_result = False
        actual_result = yesno("no")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_NO(self):
        expected_result = False
        actual_result = yesno("NO")
        self.assertEqual(actual_result, expected_result)

    def test_yesno_invalid(self):
        expected_result = True
        actual_result = yesno("SFISDNOG")
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
