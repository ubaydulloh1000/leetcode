n = int(input())


def is_prime(num):
	if num < 2:
		return False

	for i in range(2, num // 2 + 1):
		if num % i == 0:
			return False
	return True


def is_almost_prime(num):
	if num < 6:
		return False

	cnt = 0
	for i in range(2, num // 2 + 1):
		if is_prime(i) and num % i == 0:
			cnt += 1
	return cnt == 2


a_primes = 0
for i in range(1, n+1):
	if is_almost_prime(i):
		a_primes += 1


print(a_primes)
