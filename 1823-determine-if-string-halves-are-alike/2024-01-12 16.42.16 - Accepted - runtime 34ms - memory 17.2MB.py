class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        k = len(s) // 2
        A = B = 0
        for a,b in zip(s[:k], s[k:]):
            A += a in 'aeiou'
            B += b in 'aeiou'
        return A == B