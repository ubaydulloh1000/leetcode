k, n, w = [int(i) for i in input().split()]

for i in range(1, w + 1):
	n = n - i*k

if n < 0:
	print(abs(n))
else:
	print(0)
