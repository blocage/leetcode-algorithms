class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        for ind, i in enumerate(sorted(set(arr)), 1):
            d[i] = ind
        
        return [d[f] for f in arr]