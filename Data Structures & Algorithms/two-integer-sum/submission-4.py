from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = defaultdict(SortedList)
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in numsmap:
                pairidx = numsmap[remaining].pop(0)
                return [min(i,pairidx), max(i,pairidx)]
            else:
                numsmap[nums[i]].add(i)
        return []


        