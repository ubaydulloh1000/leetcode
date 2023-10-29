from collections import Counter


def is_lucky(num):
	c = Counter(str(num))
	return c.get("4", 0) + c.get("7", 0) == len(str(num))


n = int(input())

res = "NO"

for i in range(n):
	if is_lucky(n):
		res = "YES"
		break

	if is_lucky(i) and n % i == 0:
		res = "YES"
		break


print(res)
