from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

# サンプルデータ（年齢と購買額）
data = np.array([
    [25, 300], [30, 400], [35, 500],
    [45, 700], [50, 800], [60, 1200]
])

# 階層的クラスタリング
linked = linkage(data, method='ward')

# デンドログラムのプロット
dendrogram(linked, labels=["User1", "User2", "User3", "User4", "User5", "User6"])
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Users")
plt.ylabel("Distance")
plt.show()
