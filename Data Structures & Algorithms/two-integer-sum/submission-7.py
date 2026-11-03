class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _nums = {}
        print(_nums)
        for i, v in enumerate(nums):
            looking = target - v
            if looking in _nums:
                return [_nums[looking], i]
            _nums[v] = i
        return []
        