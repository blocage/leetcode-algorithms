class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles) * h
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(f / mid) for f in piles) <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo