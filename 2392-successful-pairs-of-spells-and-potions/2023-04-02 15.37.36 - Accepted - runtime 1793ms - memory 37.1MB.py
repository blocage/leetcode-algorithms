class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        l = len(potions)
        res = []
        for i in spells:
            lo, hi = 0, l
            while lo < hi:
                mid = (lo + hi) // 2
                if potions[mid] * i >= success:
                    hi = mid
                else:
                    lo = mid + 1
            
            res.append(l - lo)
        
        return res