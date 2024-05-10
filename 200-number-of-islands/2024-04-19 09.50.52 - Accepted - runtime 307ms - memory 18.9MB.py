class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        res = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1':
                    stack = [(x, y)]
                    res += 1
                    while stack:
                        X, Y = stack.pop()
                        if grid[Y][X] != '1':continue
                        grid[Y][X] = '0'
                        for i,j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                            xx = min(max(0, X - i), w - 1)
                            yy = min(max(0, Y - j), h - 1)
                            if grid[yy][xx] == '1': stack.append((xx, yy))

        return res