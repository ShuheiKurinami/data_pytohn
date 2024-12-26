from typing import List
from collections import Counter
import matplotlib.pyplot as plt
import math

num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10]

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def de_mean(xs: List[float]) -> List[float]:
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

def variance(xs: List[float]) -> float:
    deviations = de_mean(xs)
    return sum(x ** 2 for x in deviations) / (len(xs) - 1)

def standard_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

print("分散:", variance(num_friends))           # 分散
print("標準偏差:", standard_deviation(num_friends))  # 標準偏差
