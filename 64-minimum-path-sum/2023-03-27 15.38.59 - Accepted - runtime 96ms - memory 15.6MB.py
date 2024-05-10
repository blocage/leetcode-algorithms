class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, h := len(grid)):grid[i][0] += grid[i - 1][0]
        for i in range(1, w := len(grid[0])):grid[0][i] += grid[0][i - 1]
        for i in range(1, h):
            for j in range(1, w):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[h - 1][w - 1]