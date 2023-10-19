x = 0


for i in range(int(input())):
	statement = input()
	if statement[:2] == "++" or statement[1:] == "++":
		x += 1
	elif statement[:2] == "--" or statement[1:] == "--":
		x -= 1

print(x)
