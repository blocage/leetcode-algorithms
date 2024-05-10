class Solution:
    def slowestKey(self, rls: List[int], k: str) -> str:
        res = (rls[0], k[0])
        for i in range(1, len(rls)):
            res = max(res, (rls[i] - rls[i - 1], k[i]))
        
        return res[1]