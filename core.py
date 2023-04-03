import numpy as np


def calc_ema(today, prev: np.ndarray):
    numerator = today
    denominator = 1
    alpha = 2 / (len(prev) + 1)
    for i, val in enumerate(prev):
        numerator += (1 - alpha) ** (i + 1) * val
        denominator += (1 - alpha) ** (i + 1)
    return numerator / denominator


def calc_macd(prices: np.ndarray, short_period, long_period):
    macd = np.full_like(prices, np.nan)
    for i, val in enumerate(prices[:-long_period]):
        short_ema = calc_ema(val, prices[i + 1 : i + 1 + short_period])
        long_ema = calc_ema(val, prices[i + 1 : i + 1 + long_period])
        macd[i] = short_ema - long_ema
    return macd


def calc_signal(macd: np.ndarray, period):
    signal = np.full_like(macd, np.nan)
    for i, val in enumerate(macd[:-period]):
        signal[i] = calc_ema(val, macd[i + 1 : i + 1 + period])
    return signal
