from re import match, sub
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = sub(r'\*+', '*', p)
        m = match(p, s)
        if not m:
            return m
        
        return m.group(0) == s