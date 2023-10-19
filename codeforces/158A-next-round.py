n, k = [int(i) for i in input().split(" ")]


cnt = 0
scores = input().split(" ")
for i in scores:
	if int(i) > 0 and int(i) >= int(scores[k-1]):
		cnt += 1


print(cnt)
