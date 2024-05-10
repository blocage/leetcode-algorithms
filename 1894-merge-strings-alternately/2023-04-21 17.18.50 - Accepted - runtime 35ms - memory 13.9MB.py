class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        a, b = list(a)[::-1], list(b)[::-1]
        res = ''
        while a or b:
            if a:
                res += a.pop()
            if b:
                res += b.pop()
        
        return res