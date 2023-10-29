def is_good(s):
	for i in range(0, len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True


for t in range(int(input())):

	n, m = [int(i) for i in input().split()]
	str1 = input()
	str2 = input()

	if not is_good(str1) and m >= 2 and not is_good(str2):
		print("NO")
		continue

	res = "YES"
	for j in range(0, n - 1):
		if m >= 2:
			if str1[j] == str2[0] or str1[j+1] == str2[-1]:
				res = "NO"
				break
		else:
			if str1[j] == str2[0] or str[j+1] == str2[0]:
				res = "NO"
				break

	print(res)
