import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    variance = (((2 * np.mean(x) - 0.065) - 0.065) ** 2) / 12
    z = norm.ppf(1 - p / 2)
    interval = ((2 * np.mean(x) - 0.065) - z * np.sqrt(variance / n), (2 * np.mean(x) - 0.065) + z * np.sqrt(variance / n))
    return interval
