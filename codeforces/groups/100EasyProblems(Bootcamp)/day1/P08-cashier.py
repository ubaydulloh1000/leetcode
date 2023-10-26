n, L, a = [int(i) for i in input().split()]



breaks = 0
current = 0

for i in range(n):
	t, l = [int(j) for j in input().split()]
	temp = t
	breaks += (t - current) // a
	current = t + l

while L - a >= current:
	breaks += 1
	current += a


print(breaks)
