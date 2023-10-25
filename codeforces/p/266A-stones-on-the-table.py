n, stones = int(input()), input()


cnt = 0
temp = stones[0]

for i in range(1, n):
	if stones[i] == temp:
		cnt += 1
	else:
		temp = stones[i]

print(cnt)
