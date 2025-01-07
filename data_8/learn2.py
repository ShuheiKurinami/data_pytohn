import matplotlib.pyplot as plt
import numpy as np
import math
from typing import Tuple

# **1. 正規分布と信頼区間**
def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

def normal_two_sided_bounds(probability: float, mu: float, sigma: float) -> Tuple[float, float]:
    tail_probability = (1 - probability) / 2
    lower_bound = mu + sigma * math.sqrt(2) * math.erfinv(2 * tail_probability - 1)
    upper_bound = mu - sigma * math.sqrt(2) * math.erfinv(2 * (1 - tail_probability) - 1)
    return lower_bound, upper_bound

n = 1000
p = 0.5
mu, sigma = normal_approximation_to_binomial(n, p)
bounds = normal_two_sided_bounds(0.95, mu, sigma)
print(f"Normal Distribution Mean: {mu}, Sigma: {sigma}")
print(f"95% Confidence Interval: {bounds}")

# **2. ベイズ更新**
def beta_pdf(x: float, alpha: float, beta: float) -> float:
    if x <= 0 or x >= 1:
        return 0
    B = math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)
    return (x ** (alpha - 1)) * ((1 - x) ** (beta - 1)) / B

def bayesian_update(successes: int, failures: int, alpha_prior: int = 2, beta_prior: int = 2):
    alpha_posterior = alpha_prior + successes
    beta_posterior = beta_prior + failures

    x = np.linspace(0, 1, 500)
    prior = [beta_pdf(val, alpha_prior, beta_prior) for val in x]
    posterior = [beta_pdf(val, alpha_posterior, beta_posterior) for val in x]

    print(f"Prior Distribution Parameters: alpha={alpha_prior}, beta={beta_prior}")
    print(f"Posterior Distribution Parameters: alpha={alpha_posterior}, beta={beta_posterior}")

bayesian_update(successes=8, failures=2)

# **3. A/Bテスト**
def a_b_test_statistic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A = n_A / N_A
    p_B = n_B / N_B
    sigma_A = math.sqrt(p_A * (1 - p_A) / N_A)
    sigma_B = math.sqrt(p_B * (1 - p_B) / N_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

def ab_test_example():
    z = a_b_test_statistic(1000, 200, 1000, 180)
    p_value = 2 * (1 - normal_cdf(abs(z)))
    print(f"A/B Test z-score: {z:.2f}")
    print(f"p-value: {p_value:.3f}")

ab_test_example()