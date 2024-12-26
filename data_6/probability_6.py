import math

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """正規分布の累積分布関数"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# 計算例
print("mu=0, sigma=1, x=-1:", normal_cdf(-1, mu=0, sigma=1))  # 約0.158
print("mu=0, sigma=1, x=0:", normal_cdf(0, mu=0, sigma=1))    # 0.5
print("mu=0, sigma=1, x=1:", normal_cdf(1, mu=0, sigma=1))    # 約0.841
