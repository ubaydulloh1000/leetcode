username = input()

d = {i for i in username}
if len(d) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
