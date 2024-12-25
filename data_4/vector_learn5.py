friend_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
]

# ユーザー 3 の友人リスト
friends_of_3 = [i for i, is_friend in enumerate(friend_matrix[3]) if is_friend]

print(friends_of_3)  # [1, 2]
