class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, w, wl = len(s), '', 0
        for i in range(l):
            for u in (0, 1):
                j, k = i, i + u
                while j >= 0 and l > k and s[j] == s[k]:
                    j -= 1
                    k += 1

                if k - j - 1 > wl:
                    wl = k - j - 1
                    w = s[j + 1: k]

        return w
