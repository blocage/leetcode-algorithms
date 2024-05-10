class Solution:
    def countAsterisks(self, s: str) -> int:
        return ''.join(s.split('|')[::2]).count('*')