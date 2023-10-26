a, b = input().split()
a, b = int(a), int(b)

years = 0

while a <= b:
	years += 1
	a = a * 3
	b = b * 2

print(years)
