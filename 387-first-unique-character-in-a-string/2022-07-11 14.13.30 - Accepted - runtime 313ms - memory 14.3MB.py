class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = ''
        for ind, i in enumerate(s):
            if i not in s[ind + 1:] + seen:
                return ind
            seen += i
        return -1