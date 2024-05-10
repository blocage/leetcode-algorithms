class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        r = 0
        for a,b in sorted(c.items(), key=lambda x: x[1]):
            if b <= k:
                k -= b
            else:
                r += 1
        
        return r