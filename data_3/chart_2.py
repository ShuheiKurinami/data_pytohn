from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# x座標[0, 1, 2, 3, 4]高さ[num_oscars]の棒グラフをプロットする
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favarite Movies")
plt.ylabel("# of Academy Awards")

plt.xticks(range(len(movies)), movies)

plt.show()