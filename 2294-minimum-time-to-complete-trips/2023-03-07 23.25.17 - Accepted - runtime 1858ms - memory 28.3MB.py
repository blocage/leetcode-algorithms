class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, min(time) * totalTrips
        
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(mid // f for f in time) >= totalTrips:hi = mid
            else:lo = mid + 1
        
        return lo
            