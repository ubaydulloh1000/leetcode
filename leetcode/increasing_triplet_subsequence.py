class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3: 
            return False
        
        a, b = float("inf"), float("inf")
        for i in range(0, n):
            if nums[i] <= a:
                a = nums[i]
            elif nums[i] <= b:
                b = nums[i]
            else:
                return True
        return False



def main():
    nums = [2,1,5,0,4,6]
    Solution().increasingTriplet(nums)


if __name__ == '__main__':
    main()
