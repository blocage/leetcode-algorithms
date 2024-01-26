class Solution:
    def rearrangeCharacters(self, s: str, t: str) -> int:
        s = collections.Counter(s)
        t = collections.Counter(t)
        res = 1E6
        for i, c in t.items():
            if i not in s:
                return 0
            res = min(res, s[i] // c)
        
        return res