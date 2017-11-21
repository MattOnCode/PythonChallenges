import os.path

# Friendly path to file of words.
trader_data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'trader.dat'))

# Creates list of words from file excluding white spacing
trader_data_list = []
for line in open(trader_data_file, 'r').readlines():
    trader_data_list.append(float(line.strip()))


def calculate_profit(trader_data):
    """
    Calculates the total profit the trader earn't.
    :param trader_data: List of the traders data.
    :return: The total profit earn't.
    """
    total_profit = 0
    for trade in trader_data:
        total_profit += trade
    return round(total_profit, 2)


def calculate_average_profit(trader_data):
    """
    Calculates the average annual profit for the trader.
    param trader_data: List of the traders data.
    :return: The average annual profit.
    """
    profit = 0
    trade_days = int((2000/365)*(5*(365-28/7)))
    for trade_day in range(0, trade_days):
        profit += trader_data[trade_day]
    return round(profit, 2)


print("Trader Total Profit: {}".format(calculate_profit(trader_data_list)))
print("Trader average annual profit: £{}".format(calculate_average_profit(trader_data_list)))
