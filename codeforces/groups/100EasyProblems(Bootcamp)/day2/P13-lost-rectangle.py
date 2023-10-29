A = int(input())

p = float("inf")


a = int(A ** (1/2))
for i in range(1, a + 1):
	if A % i == 0:
		p = min(p, 2 * (i + A // i))


print(p)
