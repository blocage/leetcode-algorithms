class Solution:
    def partitionString(self, s: str) -> int:
        l = ''
        res = 1
        for i in s:
            if i in l:
                l = i
                res += 1
            
            else:
                l += i
        
        return res