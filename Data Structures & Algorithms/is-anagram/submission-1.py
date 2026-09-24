class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        s_counter = len(s)
        for ch in s:
            s_map[ch] = s_map.get(ch,0) + 1
        for ch in t:
            if not ch in s_map:
                return False
            elif s_map.get(ch,0) == 0:
                return False
            else:
                s_map[ch] = s_map[ch] - 1
        return True

        