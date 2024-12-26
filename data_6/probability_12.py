import random, enum
import matplotlib.pyplot as plt

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

both_girls = 0
older_girl = 0

# シミュレーションの結果を記録
results = []

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
        if younger == Kid.GIRL:
            both_girls += 1
    # 記録用
    results.append((older == Kid.GIRL, younger == Kid.GIRL))

# 条件付き確率
probability = both_girls / older_girl
print("P(both | older):", probability)

# ヒストグラムを描画
older_is_girl = [r[0] for r in results]
both_girls_count = [r[0] and r[1] for r in results]

labels = ['Older is Girl', 'Both Girls']
counts = [sum(older_is_girl), sum(both_girls_count)]

plt.bar(labels, counts, color=['blue', 'orange'])
plt.title("Condition Counts")
plt.ylabel("Count")
plt.show()
