def cal_max(nums):
	n = len(nums)

	if n == 1:
		return nums[0]

	if nums[0] > cal_max(nums[1:]):
		return nums[0]
	return cal_max(nums[1:])


def main():
	nums = [1, 4, 3, 7, 10, 29, 32, 3, 2, 43, 32]

	print(cal_max(nums))


if __name__ == '__main__':
	main()
