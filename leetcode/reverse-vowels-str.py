class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "u", "o"]

        n = len(s)
        s_vowels = []
        for i in range(n):
            if s[i] in vowels:
                s_vowels.append(s[i])

        reversed_s_vowels = s_vowels[::-1]
        result = ""
        x = 0
        for i in range(n):
            if s[i] in vowels:
                result += reversed_s_vowels[x]
                x += 1
            else:
                result += s[i]
        return result


def main():
    print(Solution().reverseVowels("leetcode"))


if __name__ == '__main__':
    main()
