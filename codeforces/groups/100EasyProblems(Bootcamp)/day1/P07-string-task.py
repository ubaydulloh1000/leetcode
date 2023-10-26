s = input()

vowels = ["a", "o", "y", "e", "u", "i"]

res = ""

for i in s:
	if i.lower() in vowels:
		continue
	else:
		res += "."
		if i.isupper():
			res += i.lower()
		else:
			res += i


print(res)
