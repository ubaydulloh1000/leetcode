def cal_len(lst):
	if not lst:
		return 0
	return 1 + cal_len(lst[1:])


def main():
	nums = [1, 4, 3, 7, 10, 29, 32, 3, 2, 43, 32]

	print(cal_len(nums))


if __name__ == '__main__':
	main()
