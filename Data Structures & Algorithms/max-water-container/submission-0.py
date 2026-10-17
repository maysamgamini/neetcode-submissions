class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        water = 0
        while l < r:
            w = r - l
            min_h = min(heights[l], heights[r])
            water = max(water, w * min_h)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return water
        