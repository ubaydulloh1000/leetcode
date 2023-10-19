n = int(input())

cap = 0
min_cap = 0

for i in range(n):
	a, b = [int(j) for j in input().split()]
	cap -= a
	cap += b
	min_cap = max(cap, min_cap)


print(min_cap)
