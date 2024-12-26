from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# サンプルデータ（購買頻度と購入金額）
data = np.array([
    [1, 200], [2, 300], [3, 500], [4, 800], [5, 900],
    [10, 2000], [11, 2200], [12, 2500]
])

# クラスタリング実行
kmeans = KMeans(n_clusters=2, random_state=0).fit(data)
labels = kmeans.labels_

# 結果をプロット
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title("Clustering Example")
plt.xlabel("Frequency")
plt.ylabel("Amount")
plt.show()
