import numpy as np


def calculate_ema(today, prev: np.ndarray):
    numerator = today
    denominator = 1
    alpha = 2 / (len(prev) + 1)
    for i, val in enumerate(prev):
        numerator += (1 - alpha) ** (i + 1) * val
        denominator += (1 - alpha) ** (i + 1)
    return numerator / denominator


def calculate_macd(prices: np.ndarray, slow_period, fast_period):
    macd = np.full_like(prices, np.nan)
    for i, val in enumerate(prices[:-fast_period]):
        np.append(macd, [i])
        slow_ema = calculate_ema(val, prices[i + 1:i + 1 + slow_period])
        fast_ema = calculate_ema(val, prices[i + 1:i + 1 + fast_period])
        macd[i] = slow_ema - fast_ema
    return macd


def calculate_signal(macd: np.ndarray, period):
    signal = np.full_like(macd, np.nan)
    for i, val in enumerate(macd[:-period]):
        signal[i] = calculate_ema(val, macd[i + 1:i + 1 + period])
    return signal
