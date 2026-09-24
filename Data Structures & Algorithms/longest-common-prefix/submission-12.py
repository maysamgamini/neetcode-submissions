class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if not strs or not strs[0]:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if not strs[0][i] == strs[-1][i]:
                return strs[0][:i]
        return strs[0]        