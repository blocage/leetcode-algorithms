class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        
        for i in range(1, h):
            grid[i][0] += grid[i - 1][0]
        
        for i in range(1, w):
            grid[0][i] += grid[0][i - 1]
        
        for i in range(1, h):
            for j in range(1, w):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
            
        
        return grid[-1][-1]