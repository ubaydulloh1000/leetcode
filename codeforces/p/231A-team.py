r = 0

for i in range(int(input())):
	if sum([int(i) for i in input().split(" ")]) >= 2:
		r+=1


print(r)
