class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]) - 1, len(grid) - 1
        visited = set()
        r = []
        for y,i in enumerate(grid):
            for x,j in enumerate(i):
                if (x,y) not in visited:
                    visit = [(x,y)]
                    size = 0
                    while visit:
                        X,Y = visit.pop()
                        if (X,Y) in visited or not grid[Y][X]:
                            continue
                        visited.add((X,Y))
                        size += 1
                        for a,b in ((1,0),(-1,0),(0,1),(0,-1)):
                            XX = max(min(X + a, w),0)
                            YY = max(min(Y + b, h),0)
                            visit.append((XX,YY))
                        
                    r.append(size)
                    
        return max(r)
        