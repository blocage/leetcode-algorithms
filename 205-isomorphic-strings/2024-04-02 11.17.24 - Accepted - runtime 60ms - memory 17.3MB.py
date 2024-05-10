class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, b = map(Counter, (s, t))
        for i in range(len(s)):
            if a[s[i]] != b[t[i]]:
                return False
        
        a, b = map(lambda x: [len(list(i)) for f,i in groupby(x)], (s, t))
        return a == b