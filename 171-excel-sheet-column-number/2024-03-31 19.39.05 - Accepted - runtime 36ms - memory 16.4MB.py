class Solution:
    def titleToNumber(self, t: str) -> int:
        res = 0
        for i in t:res = res * 26 + (ord(i) - 65 + 1)
        return res