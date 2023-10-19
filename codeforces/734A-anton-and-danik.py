from collections import Counter


n, games = int(input()), input()

c = Counter(games)

if c["A"] > c["D"]:
	print("Anton")
elif c["A"] < c["D"]:
	print("Danik")
else:
	print("Friendship")
