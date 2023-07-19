import random


def quick_sort(nums):
	n = len(nums)
	if n < 2:
		return nums

	random.shuffle(nums)
	pivot = nums[0]

	lows = [i for i in nums[1:] if i <= pivot]
	highs = [i for i in nums[1:] if i > pivot]
	
	sorted_nums = quick_sort(lows) + [pivot] + quick_sort(highs) 
	return sorted_nums


def main():
	nums = [2, 1, 5, 8, 4, 3, 9]
	print(quick_sort(nums))


if __name__ == '__main__':
	main()
