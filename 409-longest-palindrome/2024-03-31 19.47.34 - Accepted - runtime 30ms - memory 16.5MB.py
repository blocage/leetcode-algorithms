class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v % 2 for v in Counter(s).values())
        return len(s) - odds + bool(odds)