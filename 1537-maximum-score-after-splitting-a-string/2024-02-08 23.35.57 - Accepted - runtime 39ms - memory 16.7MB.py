class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:f + 1].count('0') + s[f + 1:].count('1') for f in range(len(s) - 1))