import pandas as pd
import numpy as np
from scipy.stats import t 
from scipy.stats import norm


chat_id = 277684942 

def solution(p: float, x: np.array) -> tuple:
    a = 0.065
    alpha = 1 - p
    n = len(x)
    b = np.max(x)
    interval = (b, b + t.ppf (1 - alpha, n - 1) * np.sqrt( (b - a) ** 2 /(12 * n)))
    return interval
