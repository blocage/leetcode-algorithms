class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust: return 1 if n == 1 else -1
        d, k = defaultdict(int), defaultdict(int)
        for i in trust:
            k[i[0]] += 1
            d[i[1]] += 1

        for r,v in d.items():
            if v == n - 1 and k[r] == 0: return r
        
        return -1
