class Solution:
    def trap(self, height: List[int]) -> int:
        l = w = lvl = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                low = height[l]
                l += 1
            else:
                low = height[r]
                r -= 1
            lvl = max(lvl, low)
            w += lvl - low
        
        return w
