
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp = str1 if len(str1) <= len(str2) else str2
        
        str1_n = len(str1)
        str2_n = len(str2)

        n = len(temp)
        x = 1
        
        gcd = ""
        while x <= n:
            if n % x == 0 and temp[:x] * (str1_n // x) == str1 and temp[:x] * (str2_n // x) == str2:
                gcd = temp[:x]
            x += 1
        return gcd


if __name__ == '__main__':
    test_cases = [["ABCABC", "ABC"], ["ABABAB", "ABAB"], ["LEET", "CODE"]]

    for c in test_cases:
        s = Solution().gcdOfStrings(*c)
        print(s)
