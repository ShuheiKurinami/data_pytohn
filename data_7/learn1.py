import random
import matplotlib.pyplot as plt
import numpy as np
import math
from typing import Tuple

# 二項分布を正規分布で近似する関数
def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 正規分布の確率密度関数
def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# ベータ分布のPDF
def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:
        return 0
    B = math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)
    return (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / B

# コインを1000回投げて、表が出た回数をシミュレーション
num_trials = 1000
n = 1000  # 試行回数
p = 0.5   # 表が出る確率

# 実際のシミュレーション結果
results = [sum(1 if random.random() < p else 0 for _ in range(n)) for _ in range(num_trials)]

# 二項分布の正規近似
mu, sigma = normal_approximation_to_binomial(n, p)

# グラフの準備 (正規分布 vs シミュレーション)
x = np.linspace(min(results) - 10, max(results) + 10, 500)
y = [normal_pdf(val, mu, sigma) for val in x]

plt.figure(figsize=(10, 6))
plt.hist(results, bins=30, density=True, alpha=0.6, color='blue', label='Simulated Binomial')
plt.plot(x, y, color='red', linewidth=2, label='Normal Approximation')
plt.title("Binomial Distribution vs. Normal Approximation", fontsize=14)
plt.xlabel("Number of Heads", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# ベイズ推論の可視化
def bayesian_update(successes: int, failures: int, alpha_prior: int = 2, beta_prior: int = 2):
    # 事前分布
    alpha_posterior = alpha_prior + successes
    beta_posterior = beta_prior + failures

    x = np.linspace(0, 1, 500)
    prior = [beta_pdf(val, alpha_prior, beta_prior) for val in x]
    posterior = [beta_pdf(val, alpha_posterior, beta_posterior) for val in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, prior, label='Prior Distribution', color='blue')
    plt.plot(x, posterior, label='Posterior Distribution', color='orange')
    plt.title("Bayesian Updating with Beta Distribution", fontsize=14)
    plt.xlabel("Probability of Success", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# ベイズ更新の例: 成功8回, 失敗2回
bayesian_update(successes=8, failures=2)
