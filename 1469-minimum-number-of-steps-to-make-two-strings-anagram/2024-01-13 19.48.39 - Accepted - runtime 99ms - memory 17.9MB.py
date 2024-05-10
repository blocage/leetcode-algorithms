class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = collections.Counter(t).items()
        b = collections.Counter(s)
        r = 0
        for i,j in a:
            r += max(j - b[i], 0)
        
        return r