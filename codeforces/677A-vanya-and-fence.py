n, h = [int(i) for i in input().split()]
friends = [int(i) for i in input().split()]


width = 0
for i in range(n):
	if friends[i] > h:
		width += 2
	else:
		width += 1


print(width)
