import enum, random

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

# シミュレーション
both_girls = 0
older_girl = 0

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
        if younger == Kid.GIRL:
            both_girls += 1

print("P(both | older):", both_girls / older_girl)
