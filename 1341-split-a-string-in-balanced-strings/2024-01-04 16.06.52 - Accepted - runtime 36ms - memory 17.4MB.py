class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = r = 0
        for i in s:
            c += 1 if i == 'L' else -1
            if c == 0:
                r += 1
        
        return r