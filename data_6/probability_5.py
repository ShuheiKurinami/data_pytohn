import matplotlib.pyplot as plt
import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """正規分布の確率密度関数"""
    return math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (SQRT_TWO_PI * sigma)


xs = [x / 10.0 for x in range(-50, 50)]
ys = [normal_pdf(x, mu=0, sigma=1) for x in xs]

plt.plot(xs, ys, label="mu=0, sigma=1")
plt.title("正規分布の確率密度関数")
plt.xlabel("x")
plt.ylabel("確率密度")
plt.grid(True)
plt.legend()
plt.show()
