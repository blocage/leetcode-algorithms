class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, c in collections.Counter(s).items():
            if c == 1:
                return s.index(i)
        
        return -1