class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and len(set((s[i] + s[i + 1]).lower())) == 1:
                return self.makeGood(s[:i] + s[i + 2:])
        return s