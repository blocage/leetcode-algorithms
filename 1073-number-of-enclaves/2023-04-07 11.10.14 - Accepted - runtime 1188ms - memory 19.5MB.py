class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        res = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x]:
                    stack = [(x, y)]
                    is_boundary = False
                    length = 0
                    while stack:
                        X, Y = stack.pop()
                        if not grid[Y][X]:continue
                        if X == 0 or X == w - 1 or Y == 0 or Y == h - 1:
                            is_boundary = True
                        length += 1
                        grid[Y][X] = 0
                        for i, j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                            XX = min(max(X + i, 0), w - 1)
                            YY = min(max(Y + j, 0), h - 1)
                            if grid[YY][XX]:
                                stack.append((XX, YY))
                    if not is_boundary:
                        res += length
        
        return res