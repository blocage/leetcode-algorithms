class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        return sum(s[f] != heights[f] for f in range(len(heights)))