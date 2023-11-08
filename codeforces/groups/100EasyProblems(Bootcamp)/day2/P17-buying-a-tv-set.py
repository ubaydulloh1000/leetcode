import math


a, b, x, y = [int(i) for i in input().split()]


gcd_xy = math.gcd(x, y)
x, y = x // gcd_xy, y // gcd_xy


# cnt = 0
# x_temp = 0
# y_temp = 0
# while x_temp < a and y_temp < b:
# 	x_temp += x
# 	y_temp += y

# 	if x_temp <= a and y_temp <= b:
# 		cnt += 1


# print(cnt)
print(min(a // x, b // y))
