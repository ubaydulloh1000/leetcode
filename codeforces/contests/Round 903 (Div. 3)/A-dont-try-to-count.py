for i in range(int(input())):
	n, m = [int(j) for j in input().split()]

	x, s = input(), input()
	cnt = 0

	while True:
		if s in x:
			break

		if n > 25:
			break

		x = x + x
		n = len(x)
		cnt+=1

	if s in x:
		print(cnt)
	else:
		print(-1)
	cnt = 0
