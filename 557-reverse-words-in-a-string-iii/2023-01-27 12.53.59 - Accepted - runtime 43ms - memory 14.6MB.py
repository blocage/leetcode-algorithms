class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(f[::-1] for f in s.split())