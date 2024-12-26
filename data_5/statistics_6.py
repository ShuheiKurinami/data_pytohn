from typing import List
import math

num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10]
daily_minutes = [68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, 54.01, 38.79]

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


def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "データの長さが異なります"
    return sum(x * y for x, y in zip(de_mean(xs), de_mean(ys))) / (len(xs) - 1)

def correlation(xs: List[float], ys: List[float]) -> float:
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / (stdev_x * stdev_y)
    else:
        return 0

print("共分散:", covariance(num_friends[:len(daily_minutes)], daily_minutes))
print("相関係数:", correlation(num_friends[:len(daily_minutes)], daily_minutes))
