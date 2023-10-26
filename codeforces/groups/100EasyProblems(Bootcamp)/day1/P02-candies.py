N = int(input())
s = [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]


res = 0
for i in range(a, b+1):
	res += s[i]

print(res)
