from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from macd import calculate_macd, calculate_signal, find_crosses

plt.rcParams['backend'] = 'Qt5Agg'
plt.rcParams['lines.linewidth'] = 1

SOURCE_FILENAME = 'data.csv'
RESULT_FILENAME = 'plot.jpg'


def str_to_datetime(val):
    return datetime.strptime(val, '%m/%d/%Y').date()


def price_to_float(val):
    return float(val[1:])


dates = np.loadtxt(SOURCE_FILENAME, dtype=datetime, delimiter=',',
                   converters=str_to_datetime, skiprows=1, usecols=0, encoding=None)
prices = np.loadtxt(SOURCE_FILENAME, dtype=float, delimiter=',',
                    converters=price_to_float, skiprows=1, usecols=1)

macd = calculate_macd(prices, 12, 26)
signal = calculate_signal(macd, 9)
(crosses_from_below, crosses_from_above) = find_crosses(macd, signal)

fig, (ax1, ax2) = plt.subplots(2, layout='constrained', sharex=True)

ax1.plot(dates, prices, c='tab:blue', label='Price')
ax1.set_title('Stock price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price')
ax1.legend(loc='best')

ax2.plot(dates, macd, c='tab:blue', label='MACD')
ax2.plot(dates, signal, c='tab:orange', label='Signal')
ax2.plot(dates, crosses_from_below, marker='.', c='tab:green')
ax2.plot(dates, crosses_from_above, marker='.', c='tab:red')
ax2.set_title('MACD indicator')
ax2.set_xlabel('Date')
ax2.set_ylabel('Value')
ax2.legend(loc='best')

plt.savefig(RESULT_FILENAME, dpi=600)
plt.show()
