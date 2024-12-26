import random
from collections import Counter
import matplotlib.pyplot as plt

def bernoulli_trial(p: float) -> int:
    return 1 if random.random() < p else 0

def binomial(n: int, p: float) -> int:
    return sum(bernoulli_trial(p) for _ in range(n))

# シミュレーション
n, p, num_trials = 10, 0.5, 1000
data = [binomial(n, p) for _ in range(num_trials)]

# ヒストグラムをプロット
histogram = Counter(data)
plt.bar(histogram.keys(), [v / num_trials for v in histogram.values()])
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("# of successes")
plt.ylabel("Frequency")
plt.show()
