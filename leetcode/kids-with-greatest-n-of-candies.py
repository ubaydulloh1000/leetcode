from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [True if i + extraCandies >= max_candies else False for i in candies]


def main():

    candies = [1, 2, 8, 3, 4]
    ex_candies = 5
    print(Solution().kidsWithCandies(candies, ex_candies))


if __name__ == '__main__':
    main()
