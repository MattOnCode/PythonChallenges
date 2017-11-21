import unittest
from .trade_ratio import calculate_ratio, calculate_bonus


class TestTerms(unittest.TestCase):

    def test_calculate_ratio_win(self):
        trader_data = [-10, 10, -10, 10]
        expected_result = 1
        actual_result = calculate_ratio(trader_data, "win")
        self.assertEqual(expected_result, actual_result)

    def test_calculate_ratio_loss(self):
        trader_data = [-10, 10, -10, 10, -10]
        expected_result = 1.5
        actual_result = calculate_ratio(trader_data, "lose")
        self.assertEqual(expected_result, actual_result)

    def test_calculate_ratio_loss(self):
        trader_data = [200000, -1000, 300000, -10000]
        expected_result = 1
        actual_result = calculate_bonus(trader_data)
        self.assertEqual(expected_result, len(actual_result))


if __name__ == '__main__':
    unittest.main()
