def uniform_cdf(x: float) -> float:
    """一様分布の累積分布関数"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

# 計算例
print("P(X <= -0.5):", uniform_cdf(-0.5))  # 0
print("P(X <= 0.3):", uniform_cdf(0.3))   # 0.3
print("P(X <= 1.5):", uniform_cdf(1.5))   # 1
