class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[i + 1:] + s[:i]:
                return i
        return -1
        