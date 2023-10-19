n = int(input())


dgts = 0
cnt = 0

while n > 0:
	if n % 10 in [4, 7]:
		cnt += 1
	dgts += 1
	n //= 10

if cnt in [4, 7]:
	print("YES")
else:
	print("NO")
