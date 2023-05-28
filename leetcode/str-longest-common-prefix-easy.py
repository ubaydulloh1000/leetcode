from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()

        common_prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                common_prefix += strs[0][i]
            else:
                break

        return common_prefix



if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    # strs = ["aa", "ab"]
    strs = ["c","acc","ccc"]

    solution = Solution()
    print(solution.longestCommonPrefix(strs))
