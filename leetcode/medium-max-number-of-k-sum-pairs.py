from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        
        i, j = 0, len(nums) - 1
        cnt = 0
        
        nums.sort()
        
        while i < j:
            if nums[i] + nums[j] == k:
                nums.pop(j)
                nums.pop(i)
                j-=2
                cnt+=1
            elif nums[i] + nums[j] < k:
                i+=1
            else:
                j-=1
        return cnt


def main():
	nums = [3,1,3,4,3]
	k = 6
	result = Solution().maxOperations(nums, k)
	print(result)

if __name__ == '__main__':
	main()
