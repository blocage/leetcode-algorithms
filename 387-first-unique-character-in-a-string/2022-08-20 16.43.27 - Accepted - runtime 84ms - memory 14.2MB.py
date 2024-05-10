class Solution:
    def firstUniqChar(self, s: str) -> int:
        checked = ''
        for ind,i in enumerate(s):
            if i in checked: continue
            if s.count(i) == 1:return ind
            checked += i
        return -1