class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * ( 2 * len(nums))
        reader = 0
        writer = 0
        while writer < len(result):
            result[writer] = nums[reader % len(nums)]
            reader += 1
            writer += 1
        return result
        