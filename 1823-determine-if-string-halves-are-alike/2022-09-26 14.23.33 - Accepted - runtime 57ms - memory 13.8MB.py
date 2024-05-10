class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s := s.upper()) // 2
        return sum((a in 'AEIOU') - (b in 'AEIOU')for a,b in zip(s[:l], s[l:])) == 0