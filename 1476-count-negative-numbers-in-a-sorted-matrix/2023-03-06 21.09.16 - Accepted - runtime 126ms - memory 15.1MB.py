class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(sum(i < 0 for i in f) for f in grid)