from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from macd import calculate_macd, calculate_signal

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

fig1, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(dates, prices, color='g', label='Price $')
ax1.legend(loc='best')

ax2.plot(dates, macd, color='r', label='MACD')
ax2.plot(dates, signal, color='b', label='Signal')
ax2.legend(loc='best')

plt.savefig(RESULT_FILENAME, dpi=600)
