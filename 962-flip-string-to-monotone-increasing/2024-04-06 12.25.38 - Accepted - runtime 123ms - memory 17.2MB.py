class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        a = b = 0
        for i in s:
            if i == '1': a += 1
            else: b += 1
            b = min(a, b)
        
        return b