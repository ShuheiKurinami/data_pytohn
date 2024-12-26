import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """正規分布の確率密度関数"""
    return math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (SQRT_TWO_PI * sigma)

# 計算例
print("mu=0, sigma=1, x=-1:", normal_pdf(-1, mu=0, sigma=1))  # 約0.242
print("mu=0, sigma=1, x=0:", normal_pdf(0, mu=0, sigma=1))    # 約0.399
print("mu=1, sigma=2, x=1:", normal_pdf(1, mu=1, sigma=2))    # 約0.199
