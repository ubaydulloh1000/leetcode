class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False
            
        sum = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                sum = sum + i + num / i
            i+=1

        return sum == num


def main():
    n = 99999993
    print(Solution().checkPerfectNumber(n))


if __name__ == '__main__':
    main()
