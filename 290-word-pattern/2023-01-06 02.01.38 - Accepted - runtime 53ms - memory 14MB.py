class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = s.split()
        return all(p.index(a) == s.index(b)for a,b in zip(p, s)) if len(s) == len(p) else False