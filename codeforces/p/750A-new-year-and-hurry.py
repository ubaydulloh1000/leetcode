n, k = [int(i) for i in input().split()]


minutes = 4 * 60 - k


i = 0
while i < n:
	minutes -= (i+1) * 5
	if minutes < 0:
		break
	i+=1

print(i)
