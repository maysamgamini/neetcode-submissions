class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        l = [ 1] * m
        r = [ 1] * m
        
        for i in range(1, m):
            l[i] = l[i - 1] * nums[i - 1]
            r[m - i - 1] *= r[m - i] * nums[m - i]
        result = []

        for i in range(m):
            result.append(l[i] * r[i])
        return result