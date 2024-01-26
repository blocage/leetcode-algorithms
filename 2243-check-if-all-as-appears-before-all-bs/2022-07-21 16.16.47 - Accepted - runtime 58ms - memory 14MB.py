class Solution:
    def checkString(self, s: str) -> bool:
        return ''.join(sorted(s)) == s
        