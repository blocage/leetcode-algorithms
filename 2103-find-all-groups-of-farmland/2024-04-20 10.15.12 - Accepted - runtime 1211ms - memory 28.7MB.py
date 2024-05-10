class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        h, w = len(land), len(land[0])
        res = []
        for y in range(h):
            for x in range(w):
                if land[y][x]:
                    stack = [(x, y)]
                    xi, yi = x, y
                    while stack:
                        X, Y = stack.pop()
                        if not land[Y][X]:continue
                        land[Y][X] = 0
                        for i,j in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                            xx = min(max(0, X + i), w - 1)
                            yy = min(max(0, Y + j), h - 1)
                            if land[yy][xx]:
                                xi, yi = max((xi, yi), (xx, yy))
                                stack.append((xx, yy))
                    
                    res.append((y, x, yi, xi))
        
        return res