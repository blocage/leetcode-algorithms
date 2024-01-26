class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w, h = len(grid[0]), len(grid)
        visited = [[0] * w for _ in range(h)]
        rivers = 0
        for y,i in enumerate(grid):
            for x,j in enumerate(i):
                if not visited[y][x]:
                    visit = [(x,y)]
                    size = 0
                    while visit:
                        X,Y = visit.pop()
                        if visited[Y][X] or grid[Y][X] == '0':continue
                        visited[Y][X] = 1
                        size = 1
                        for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                            XX = max(min(X + a, w - 1), 0)
                            YY = max(min(Y + b, h - 1), 0)
                            if not visited[YY][XX] and grid[YY][XX] == '1':
                                visit.append((XX,YY))
                    
                    rivers += size
                        
                        
        return rivers