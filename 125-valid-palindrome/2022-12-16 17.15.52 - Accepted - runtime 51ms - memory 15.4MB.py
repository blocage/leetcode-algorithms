class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(f for f in s.upper() if f.isalnum())
        l, r = 0, len(s) - 1
        while r > l:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True