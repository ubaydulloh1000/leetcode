players = input()


temp1 = 0
temp2 = 0

for i in players:
	if i == "0":
		temp1 += 1
		if temp2 >= 7:
			break
		temp2 = 0
	else:
		temp2 += 1
		if temp1 >= 7:
			break
		temp1 = 0


if temp1 >= 7 or temp2 >= 7:
	print("YES")
else:
	print("NO")
