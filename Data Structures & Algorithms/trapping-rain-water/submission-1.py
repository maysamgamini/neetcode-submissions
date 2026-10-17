class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, max_left = 0 , height[0]
        r, max_right =  n - 1, height[ n - 1]
        water = 0 
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                water += max_right - height[r]
        return water