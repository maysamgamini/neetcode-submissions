class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _group = defaultdict(list)
        for _str in strs:
            key = "".join(sorted(_str))
            _group[key].append(_str)
        return list(_group.values())
        