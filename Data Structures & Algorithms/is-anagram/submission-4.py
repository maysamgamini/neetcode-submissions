class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _s = [0] * 26
        _t = [0] * 26
        for i in range(len(s)):
            chs = ord(s[i]) - ord("a")
            cht = ord(t[i]) - ord("a")
            _s[chs] += 1
            _t[cht] += 1
        return _s == _t        
        