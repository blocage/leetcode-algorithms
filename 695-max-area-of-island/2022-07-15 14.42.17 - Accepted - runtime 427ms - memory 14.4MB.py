class Solution:
    def neighbours(self, x, y, grid, visited, w, h):
        neigh = []
        for a,b in ((0,1),(0,-1),(1,0),(-1,0)):
            X = max(min(x + a, w), 0)
            Y = max(min(y + b, h), 0)
            if grid[Y][X] and not visited[Y][X]:
                neigh.append((X,Y))
        return neigh
    
    def bfs(self, x, y, grid, visited, w, h, res = 0):
        visit = [(x,y)]
        while visit:
            X,Y = visit.pop()
            if visited[Y][X] or not grid[Y][X]:continue
            visited[Y][X] = 1
            visit.extend(self.neighbours(X, Y, grid, visited, w, h))
            res += grid[Y][X]
        
        return res
            
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        visited = [[0] * w for f in range(h)]
        r = []
        for y,i in enumerate(grid):
            for x,j in enumerate(i):
                if not visited[y][x]:
                    r.append(self.bfs(x,y,grid,visited,w-1,h-1))
        return max(r)
        