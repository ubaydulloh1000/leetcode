def cal_sum(nums):
	if len(nums) == 0:
		return 0
	return nums[0] + cal_sum(nums[1:])


def main():
	nums = [1, 4, 3, 7, 10]

	print(cal_sum(nums))


if __name__ == '__main__':
	main()
