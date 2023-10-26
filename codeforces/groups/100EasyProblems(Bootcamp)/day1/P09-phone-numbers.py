n, digits = int(input()), input()



eights = 0
for i in digits:
	if int(i) == 8:
		eights += 1


print(min(eights, n // 11))
