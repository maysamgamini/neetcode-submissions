class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        for idx, val in enumerate(nums):
            lookingfor = target - val
            if lookingfor in remaining:
                return [remaining[lookingfor],idx]
            else:
                remaining[val] = idx
        return []
        