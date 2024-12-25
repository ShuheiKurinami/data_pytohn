from typing import List
from collections import Counter
import matplotlib.pyplot as plt

# データの準備
num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11, 10, 10]


# ヒストグラム
friend_counts = Counter(num_friends)
xs = range(int(max(num_friends)) + 1)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.title("ヒストグラム: 友人数の分布")
plt.xlabel("友人数")
plt.ylabel("人数")
plt.show()
