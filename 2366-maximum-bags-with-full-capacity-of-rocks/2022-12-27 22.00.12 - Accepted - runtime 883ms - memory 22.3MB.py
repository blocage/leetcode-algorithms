class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], r: int) -> int:
        res = 0
        for i in sorted(a - b for a,b in zip(capacity, rocks)):
            r -= i
            if r < 0:
                return res
            res += 1

        return res