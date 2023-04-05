import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 277684942 


def solution(p: float, x: np.array) -> tuple:
    alpha1 = (1 - p) / 2
    alpha2 = (1 + p) / 2
    n = x.size
    a1, a2 = pow(alpha1, 1 / n), pow(alpha2, 1 / n)

    x_max = x.max()
    return (x_max - 0.065) / a2 + 0.065, \
           (x_max - 0.065) / a1 + 0.065
