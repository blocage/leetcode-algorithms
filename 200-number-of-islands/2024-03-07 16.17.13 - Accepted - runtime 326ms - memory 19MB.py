class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        visited = [[False] * w for _ in range(h)]
        res = 0
        for y in range(h):
            for x in range(w):
                res += not visited[y][x] and grid[y][x] == '1'
                stack = [(x, y)] if grid[y][x] == '1' else []
                while stack:
                    X, Y = stack.pop()
                    if visited[Y][X]: continue
                    visited[Y][X] = True
                    for XX, YY in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        xs = min(max(0, X + XX), w - 1)
                        ys = min(max(0, Y + YY), h - 1)
                        if grid[ys][xs] == '1':
                            stack.append((xs, ys))
        
        return res
