class Solution:
    def distanceBetweenBusStops(self, d: List[int], s: int, t: int) -> int:
        a,b = sorted((s,t))
        return min(sum(d[a:b]), sum(d) - sum(d[a:b]))