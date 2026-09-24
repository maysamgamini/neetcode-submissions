class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_count = {}
        for i in range(len(nums)):
            if map_count.get(nums[i],0) + 1 > 1:
                return True 
            map_count[nums[i]] = 1
        return False