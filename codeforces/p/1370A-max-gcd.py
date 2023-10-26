
# def get_gcd(a, b):
# 	less = min(a, b)

# 	while less > 0:
# 		if a % less == 0 and b % less == 0:
# 			break
# 		less -= 1
# 	return less

import math

for t in range(int(input())):
	n = int(input())
	max_gcd = 0
	left, right = 1, n

	while left < right:
		max_gcd = max(math.gcd(left, right), max_gcd)
		left += 1
		right -= 1

	print(max_gcd)
