class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = set(arr)
        res = 1
        while k:
            if res not in l:
                k -= 1
            res += 1
        
        return res - 1