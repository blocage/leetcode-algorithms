class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        for i in s:
            if i == '*':
                res = res[:-1]
            else:
                res += i
        
        return res