class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        res = 0
        for y,i in enumerate(grid):
            for x,j in enumerate(i):
                if grid[y][x] != -1:
                    visit = [(x,y)]
                    size = 0
                    while visit:
                        X,Y = visit.pop(0)
                        if grid[Y][X] != 1:continue
                        grid[Y][X] = -1
                        size += 1
                        for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                            XX = max(min(X + a, w - 1), 0)
                            YY = max(min(Y + b, h - 1), 0)
                            if grid[YY][XX] == 1:visit.append((XX,YY))
                    res = max(size, res)
                            
                        
        
        return res