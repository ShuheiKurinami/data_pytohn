import math
import matplotlib.pyplot as plt

# 正規分布の累積分布関数 (CDF)
def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """正規分布の累積分布関数"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# x軸の値を生成
xs = [x / 10.0 for x in range(-50, 50)]  # -5.0 から 5.0 まで

# 異なる分布の累積分布関数 (CDF) を計算
ys_mu0_sigma1 = [normal_cdf(x, mu=0, sigma=1) for x in xs]  # 標準正規分布
ys_mu0_sigma2 = [normal_cdf(x, mu=0, sigma=2) for x in xs]  # 標準偏差が大きい
ys_mu1_sigma1 = [normal_cdf(x, mu=1, sigma=1) for x in xs]  # 平均値がずれている

# グラフを描画
plt.plot(xs, ys_mu0_sigma1, label="mu=0, sigma=1")
plt.plot(xs, ys_mu0_sigma2, label="mu=0, sigma=2", linestyle="--")
plt.plot(xs, ys_mu1_sigma1, label="mu=1, sigma=1", linestyle=":")
plt.title("正規分布の累積分布関数 (CDF)")
plt.xlabel("x")
plt.ylabel("P(X <= x)")
plt.legend()
plt.grid(True)
plt.show()
