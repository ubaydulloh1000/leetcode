n = int(input())
s = [int(i) for i in input().split()]


left, right = 0, 0
max_inc = 1

while right < n:
	right += 1

	if s[right] > s[right - 1]:
		temp = right - left
		max_inc = max(temp, max_inc)

	else:
		left = right
		temp = 0


print(max_inc)
