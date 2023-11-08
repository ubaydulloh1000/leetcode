n = int(input())


if n % 2 == 0:
	res = ' '.join(["2"] * (n // 2))
	print(n // 2)
	print(res)
else:
	res = ' '.join(["2"] * ((n - 3) // 2))
	print((n - 3) // 2 + 1)
	print(res + ' 3')
