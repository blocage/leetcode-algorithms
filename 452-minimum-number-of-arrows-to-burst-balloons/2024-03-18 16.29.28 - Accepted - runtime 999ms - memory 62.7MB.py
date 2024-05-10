class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res, b = 1, points[0][1]
        for s, e in points:
            if b < s:
                b = e
                res += 1

        return res  