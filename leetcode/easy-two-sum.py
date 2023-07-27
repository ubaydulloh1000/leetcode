from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        d = dict()
        
        for i in range(n):
            x = target - nums[i]
            
            if nums[i] in d.keys():
                return [d[nums[i]], i]
            else:
                d[x] = i


def main():
    print(Solution().twoSum([2,7,11,15], 9))


if __name__ == '__main__':
    main()
