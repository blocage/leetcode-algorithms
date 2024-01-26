class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(f for f in s.lower() if f.isalnum())
        return s == s[::-1]