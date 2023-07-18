from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        result = []
        
        def is_self_dividing(num):
            while num > 0:
                if num % (num % 10) != 0:
                    return False
                num = num // 10
                
            return True
        
        for i in range(left, right + 1):
            if i % 10 != 0 and "0" not in str(i):
                if is_self_dividing(i):
                    print(i)
                    result.append(i)
        return result


def main():
    print(Solution().selfDividingNumbers(23, 2901))


if __name__ == '__main__':
    main()
