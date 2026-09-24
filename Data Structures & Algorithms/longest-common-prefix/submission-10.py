class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if not strs or not strs[0]:
            return ""
        if len(strs) == 1:
            return strs[0]
        idx = 0
        for i in range(0, min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                idx = i + 1
            else:
                break
            
        return strs[0][:idx]        