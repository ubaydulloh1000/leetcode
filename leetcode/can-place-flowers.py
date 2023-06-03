from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        len_f = len(flowerbed)

        for i in range(len_f):
            if not flowerbed[i] and (i == 0 or flowerbed[i-1] == 0) and (i == len_f - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return not n > 0


def main():
    flowerbed = [1,0,0,0,0,1]
    print(Solution().canPlaceFlowers(flowerbed, 2))


if __name__ == '__main__':
    main()
