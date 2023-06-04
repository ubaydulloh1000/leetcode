class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = " ".join([i.strip() for i in s.strip().split()[::-1]])
        return reversed


def main():
    s = "a good      example"
    print(Solution().reverseWords(s))


if __name__ == '__main__':
    main()
