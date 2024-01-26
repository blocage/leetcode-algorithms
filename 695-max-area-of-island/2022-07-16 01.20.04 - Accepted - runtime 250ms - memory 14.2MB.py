class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        visited = [[0] * w for f in range(h)]
        areas = []
        for y,i in enumerate(grid):
            for x,j in enumerate(i):
                if not visited[y][x]:
                    visit = [(x,y)]
                    size = 0
                    while visit:
                        X,Y = visit.pop(0)
                        if visited[Y][X] or not grid[Y][X]:continue
                        visited[Y][X] = 1
                        size += grid[Y][X]
                        for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                            XX = max(min(X + a, w - 1), 0)
                            YY = max(min(Y + b, h - 1), 0)
                            if not visited[YY][XX] and grid[YY][XX]:
                                visit.append((XX,YY))
                    areas.append(size)
                            
                        
        
        return max(areas)