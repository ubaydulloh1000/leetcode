m = [[0] * 5] * 5
b_i, b_j = 0, 0

for i in range(5):
	row = [int(temp) for temp in input().split()]

	for j in range(5):
		if row[j] == 1:
			b_i, b_j = i, j
		m[i][j] = row[j]

print(abs(b_i - 2) + abs(b_j - 2))
