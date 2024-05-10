class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        w, h = len(grid[0]), len(grid)
        visited = [[False] * w for f in range(h)]
        res = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1' and not visited[y][x]:
                    res += 1
                    stack = [(x, y)]
                    while stack:
                        X, Y = stack.pop()
                        if visited[Y][X]:continue
                        visited[Y][X] = True
                        for XX, YY in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                            xx = min(max(0, X + XX), w - 1)
                            yy = min(max(0, Y + YY), h - 1)
                            if grid[yy][xx] == '1':
                                stack.append((xx, yy))
        
        return res
