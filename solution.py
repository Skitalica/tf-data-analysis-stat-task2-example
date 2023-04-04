import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 277684942 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    lower = np.min(x) / (1 - np.sqrt(1 - p))
    upper = np.max(x) / (1 - np.sqrt(1 - p))
    return (lower, upper)
