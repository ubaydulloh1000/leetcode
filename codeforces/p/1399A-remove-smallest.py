for t in range(int(input())):
	n = int(input())
	a = [int(i) for i in input().split()]

	a.sort()
	i = 0
	while i < n - 1:
		if abs(a[i] - a[i+1]) <= 1:
			if a[i] < a[i+1]:
				a.pop(i)
			else:
				a.pop(i+1)
			n -= 1
		else:
			i += 1

	res = "YES" if n == 1 else "NO"
	print(res)
