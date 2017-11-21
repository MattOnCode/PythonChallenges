import unittest
import random
from .trade_annual_profit import calculate_profit, calculate_average_profit


class TestTerms(unittest.TestCase):

    def test_calculate_profit(self):
        trader_data = [-10, 10, -10, 10, 5000]
        expected_result = 5000
        actual_result = calculate_profit(trader_data)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_average_profit(self):
        trader_data = []
        for x in range(10000):
            trader_data.append(random.randint(-2000, 2000))
        actual_result = calculate_average_profit(trader_data)
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
