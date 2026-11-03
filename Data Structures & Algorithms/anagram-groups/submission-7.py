class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _group = {}
        for _str in strs:
            key = "".join(sorted(_str))
            _group[key] = _group.get(key,[])
            _group[key].append(_str)
        return list(_group.values())
        