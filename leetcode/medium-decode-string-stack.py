from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = deque()
        num_stack = deque()

        result = []
        k = 0
        temp = ""

        for char in s:
            if char.isdigit():
                k += k * 10 + int(char)

            elif char == "[":
                num_stack.append(k)
                k = 0

            elif char == "]":
                result.append(int(k) * temp)
                temp = ''
                k = ''

            else:
                temp += char

        return ''.join(result)


def main():
    s1 = "3[a]2[bc]"
    s2 = "3[a2[c]]"

    print(Solution().decodeString(s1))

   
if __name__ == '__main__':
    main()
