"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
THIS IS TASK 10 WORKSHOP 3 BTW
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

General Flow of program:

Gets the file
Puts the file into a list without white spacing
Converts each item within the list into floats

variable of profit
variable of wins (increment by 1)
variable of loss (increment by 1)
for value in the list
check whether it's win or loss then increment appropriate variable
add value to the profit
check whether profit is £400,00, state bonus for the day and then reset profit.

Calculate the ratio
return the ratio

"""
import os.path

# Friendly path to file of words.
trader_data = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Resources', 'trader.dat'))

# Creates list of words from file excluding white spacing
trader_data_list = []
for line in open(trader_data, 'r').readlines():
    trader_data_list.append(float(line.strip()))


bonus_total = 0
win_total = 0
loss_total = 0
profit_total = 0
profit = 0
trade_day = 0
for value in trader_data_list:
    trade_day += 1

    if value > 0:
        win_total += 1
    else:
        loss_total += 1

    profit += value
    profit_total += value

    if profit >= 4000000:
        print("Bonus received on day {}!".format(trade_day))
        bonus_total += 1
        profit = 0

print("\nStatistics:")
print("Total Stakes Lost: {}\nTotal Stakes Won: {}\nTotal Bonuses Given: {}".format(loss_total, win_total, bonus_total))
print("Total Profit: £{}".format(round(profit_total, 2)))
