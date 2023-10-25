y = int(input())


i = y
while True:
	if i > y and len(set(str(i))) == 4:
		break
	i += 1


print(i)
