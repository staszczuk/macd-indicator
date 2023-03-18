from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

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

plt.plot(dates, prices)
plt.savefig(RESULT_FILENAME)
