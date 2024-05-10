class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ind,i in enumerate(s):
            if s.count(i) == 1:return ind
        return -1