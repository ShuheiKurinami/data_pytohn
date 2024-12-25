from typing import List
from collections import Counter
import matplotlib.pyplot as plt

# データの準備
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10]


def median(xs: List[float]) -> float:
    sorted_xs = sorted(xs)
    mid = len(xs) // 2
    if len(xs) % 2 == 0:
        return (sorted_xs[mid - 1] + sorted_xs[mid]) / 2
    else:
        return sorted_xs[mid]

def quantile(xs: List[float], p: float) -> float:
    """p分位点の計算"""
    index = int(p * len(xs))
    return sorted(xs)[index]

print("中央値:", median(num_friends))           # 中央値
print("25%点:", quantile(num_friends, 0.25))    # 25%点
print("75%点:", quantile(num_friends, 0.85))    # 75%点
