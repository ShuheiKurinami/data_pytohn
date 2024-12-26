import matplotlib.pyplot as plt


def uniform_cdf(x: float) -> float:
    """一様分布の累積分布関数"""
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

# U(0, 1) の一様分布
xs = [x / 10.0 for x in range(-10, 20)]  # -1.0 ~ 2.0 の範囲
ys = [uniform_cdf(x) for x in xs]

plt.plot(xs, ys, label="U(0, 1)")
plt.title("Uniform Distribution CDF")
plt.xlabel("x")
plt.ylabel("P(X <= x)")
plt.grid(True)
plt.legend()
plt.show()
