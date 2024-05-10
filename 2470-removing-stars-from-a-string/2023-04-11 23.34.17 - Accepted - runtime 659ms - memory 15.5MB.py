class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        for a,b in itertools.groupby(s):
            b = len(list(b))
            if a == '*':
                res = res[:-b]
            else:
                res += a * b
        
        return res