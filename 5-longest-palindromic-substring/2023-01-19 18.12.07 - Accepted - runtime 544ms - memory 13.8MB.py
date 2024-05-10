class Solution:
    def longestPalindrome(self, s: str) -> str:
        ll = len(s)
        res = ''
        wl = 0
        for i in range(ll):
            for j in (0, 1):
                l = i
                r = i + j
                while r < ll and l >= 0 and s[l] == s[r]:
                    if r - l + 1 > wl:
                        wl = r - l + 1
                        res = s[l:r + 1]
                    l -= 1
                    r += 1
        return res