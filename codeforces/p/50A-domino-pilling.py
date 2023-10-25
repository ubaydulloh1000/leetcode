M, N = (int(i) for i in input().split())

print(M * N // 2 if M * N % 2 == 0 else ((M * N) - 1) // 2)
