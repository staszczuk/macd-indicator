import numpy as np


def calculate_ema(today, prev: np.ndarray):
    numerator = today
    denominator = 1
    alpha = 2 / (len(prev) + 1)
    for i, val in enumerate(prev, start=1):
        numerator += (1 - alpha) ** (i) * val
        denominator += (1 - alpha) ** (i)
    return numerator / denominator


def calculate_macd(prices: np.ndarray, short_period, long_period):
    macd = np.full_like(prices, np.nan)
    for i, val in enumerate(prices[:-long_period], start=1):
        short_ema = calculate_ema(val, prices[i:i + short_period])
        long_ema = calculate_ema(val, prices[i:i + long_period])
        macd[i - 1] = short_ema - long_ema
    return macd


def calculate_signal(macd: np.ndarray, period):
    signal = np.full_like(macd, np.nan)
    for i, val in enumerate(macd[:-period], start=1):
        signal[i - 1] = calculate_ema(val, macd[i:i + period])
    return signal
