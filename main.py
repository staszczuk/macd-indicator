from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

import helpers
import core

plt.rcParams["backend"] = "Qt5Agg"
plt.rcParams["lines.linewidth"] = 1

SOURCE_FILENAME = "data.csv"
RESULT_FILENAME = "plot.jpg"

# load data from csv file

dates = np.loadtxt(
    SOURCE_FILENAME,
    dtype=datetime,
    delimiter=",",
    converters=helpers.str_to_datetime,
    skiprows=1,
    usecols=0,
    encoding=None,
)
prices = np.loadtxt(
    SOURCE_FILENAME,
    dtype=float,
    delimiter=",",
    converters=helpers.price_to_float,
    skiprows=1,
    usecols=1,
)

# calculate indicators

macd = core.calc_macd(prices, 12, 26)
signal = core.cal_signal(macd, 9)
(buy_signals, sell_signals) = core.find_crosses(macd, signal)

# plot data

fig, (ax1, ax2) = plt.subplots(2, layout="constrained", sharex=True)

ax1.plot(dates, prices, c="tab:blue", label="Price")
ax1.set_title("Stock price")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price")
ax1.legend(loc="best")

ax2.plot(dates, macd, c="tab:blue", label="MACD")
ax2.plot(dates, signal, c="tab:orange", label="Signal")
ax2.plot(dates, buy_signals, marker=".", c="tab:green")
ax2.plot(dates, sell_signals, marker=".", c="tab:red")
ax2.set_title("MACD indicator")
ax2.set_xlabel("Date")
ax2.set_ylabel("Value")
ax2.legend(loc="best")

plt.savefig(RESULT_FILENAME, dpi=600)
plt.show()
