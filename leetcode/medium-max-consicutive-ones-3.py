from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        max_ones = 0
        zero_count = 0  # pass up to 3 0's
        left = 0
        
        for right in range(n):
            if nums[right] == 0:
                zero_count += 1
                
                while zero_count > k:
                    if nums[left] == 0:                
                        zero_count -= 1
                    left += 1

            max_ones = max(right-left+1, max_ones)
        return max_ones


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        max_ones = 0
        zero_count = 0  # pass up to k 0's
        left, right = 0, 0
        increment_0 = True

        while right < n:
            
            if nums[right] == 1:
                right += 1
            else:
                if increment_0:
                    zero_count += 1
                    
                if zero_count > k:
                    increment_0 = False
                    
                    if nums[left] == 0:
                        zero_count-=1
                    left+=1
                else:
                    right += 1
                    increment_0 = True

            max_ones = max(max_ones, right-left)
        return max_ones



def main():
    # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    r1 = Solution().longestOnes(nums, k)
    r2 = Solution2().longestOnes(nums, k)

    print(r1)
    print(r2)

if __name__ == '__main__':
    main()
