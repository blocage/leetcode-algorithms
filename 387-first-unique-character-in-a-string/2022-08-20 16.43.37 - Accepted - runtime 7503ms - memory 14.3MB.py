class Solution:
    def firstUniqChar(self, s: str) -> int:
        checked = ''
        for ind,i in enumerate(s):
            if s.count(i) == 1:return ind
            checked += i
        return -1