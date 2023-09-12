from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        s = ""

        temp_n = 1
        for i in range(len(chars)):
            if n > i + 1 and chars[i] == chars[i + 1]:
                temp_n += 1
            else:
                if temp_n > 1:
                    s = s + "".join([chars[i], *str(temp_n).split()])
                else:
                    s = s + chars[i]
                temp_n = 1
        del chars[:]
        chars.extend([*s])
        return len(chars)



def main():
    chars = ["s", "s", "s","s", "s", "s","s", "s", "s","s", "s", "s", "a", "a", "b", "d", "d"]
    print("RESULT: ", Solution().compress(chars))


if __name__ == '__main__':
    main()
