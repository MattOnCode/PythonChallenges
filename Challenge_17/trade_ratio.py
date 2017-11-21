import os.path

# Friendly path to file of words.
trader_data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'trader.dat'))

# Creates list of words from file excluding white spacing
trader_data_list = []
for line in open(trader_data_file, 'r').readlines():
    trader_data_list.append(float(line.strip()))


def calculate_ratio(trader_data, win_or_lose="win"):
    """
    Calculates the ratio of wins or losses.
    :param win_or_lose: What to calculate the ratio for, for example ratio of wins.
    :param trader_data: List of the traders data.
    :return: The ratio.
    """
    win_total, lose_total = 0, 0
    for trade in trader_data:
        if trade > 0:
            win_total += 1
        else:
            lose_total += 1
    return round(win_total/lose_total, 3) if win_or_lose.lower() == "win" else round(lose_total/win_total, 3)


def calculate_bonus(trader_data):
    """
    Calculates which days a bonus was received for the trader.
    :param trader_data: List of the traders data.
    :return: A list containing days of which bonus was awarded.
    """
    profit = 0
    day = 0
    bonus_days = []
    for trade in trader_data:
        profit += trade
        day += 1
        if profit >= 400000:
            bonus_days.append(day)
            profit = 0
    return bonus_days


for bonus in calculate_bonus(trader_data_list):
    print("Bonus received on day {}".format(bonus))
print("Trader Winning Ratio: {}".format(calculate_ratio(trader_data_list, "win")))
