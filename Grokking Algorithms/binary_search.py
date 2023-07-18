
def binary_search(items, item):
	n = len(items)
	low = 0
	high = n - 1

	while low <= high:
		mid = (low + high) // 2

		if items[mid] == item:
			return mid
		elif items[mid] < item:
			low = mid + 1
		else:
			high = mid - 1


def main():
	items = [1, 3, 5, 7, 8, 9, 11, 13, 18, 20, 22]
	print(binary_search(items, 13))


if __name__ == '__main__':
	main()
