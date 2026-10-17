class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers) - 1
        while l < r:
            running_sum = numbers[l] + numbers[r]
            if running_sum == target:
                return [l + 1, r + 1]
            elif running_sum < target:
                l += 1
            else:
                r -= 1
        return []
        