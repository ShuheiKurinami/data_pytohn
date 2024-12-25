import numpy as np

# 友人関係を表す隣接行列
friend_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
])

# 1. 各ユーザーの友だち数
degree = friend_matrix.sum(axis=1)
print("Degree (friend counts):", degree.tolist())

# 2. 2次近傍の数 (友だちの友だち)
#   A^2を計算し、対角成分を除くことで2次近傍の数を求められる（自分自身を除く場合）
two_step = np.linalg.matrix_power(friend_matrix, 2)
# 対角成分（自分への経路）をゼロにする
np.fill_diagonal(two_step, 0)
print("Two-step neighbors:\n", two_step)

# 3. 各ユーザーの次数中心性
#   次数を最大次数で割った値
degree_centrality = degree / degree.max()
print("Degree centrality:", degree_centrality.tolist())

# ユーザー3の友人リスト（例のコード）
friends_of_3 = [i for i, is_friend in enumerate(friend_matrix[3]) if is_friend]
print("Friends of user3:", friends_of_3)
