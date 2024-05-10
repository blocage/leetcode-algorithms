class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        r = 0
        for i in range(len(points) - 1):
            x,y = points[i]
            X,Y = points[i + 1]
            r += max(abs(x - X), abs(y - Y))
            
        return r