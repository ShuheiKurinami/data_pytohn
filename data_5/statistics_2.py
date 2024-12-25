from typing import List
from collections import Counter
import matplotlib.pyplot as plt

# データの準備
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10]

# 基本統計量
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

print("平均:", mean(num_friends))               # 平均
print("最大値:", max(num_friends))              # 最大値
print("最小値:", min(num_friends))              # 最小値
print("範囲:", data_range(num_friends))         # 範囲
