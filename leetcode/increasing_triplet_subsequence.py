class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 0
        left = max(nums)
        middle = max(nums)
            
        while i < n:
            right = nums[i]
            if left >= right:
                left = right
            elif middle >= right:
                middle = right
            elif left < 
            i++


def main():
    nums = [2,1,5,0,4,6]
    Solution().increasingTriplet(nums)


if __name__ == '__main__':
    main()
