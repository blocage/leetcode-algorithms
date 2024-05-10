class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1
