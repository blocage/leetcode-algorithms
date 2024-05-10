class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                t = s[i: j + 1]
                c += t == t[::-1]
        
        return c
        