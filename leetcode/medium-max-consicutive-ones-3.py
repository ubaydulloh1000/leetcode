from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        max_ones = 0
        temp = 0
        temp_k = 0  # pass up to 3 0's
        
        for i in range(n):
            if nums[i]:
                temp += 1
            else:
                if temp_k < k:
                    temp += 1
                    temp_k += 1
                else:
                    temp = 0
                    temp_k = 0
            max_ones = max(temp, max_ones)
            print("TEMP: ", temp)
            print("MAX ONES: ", max_ones)

        return max_ones


def main():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    r = Solution().longestOnes(nums, k)
    print(r)

if __name__ == '__main__':
    main()
