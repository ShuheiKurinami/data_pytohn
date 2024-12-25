a = [2, 4, 6]
b = [1, -1, 3]

sum_vector = [x + y for x, y in zip(a, b)]

result = [2 * v for v in sum_vector]

print(result)