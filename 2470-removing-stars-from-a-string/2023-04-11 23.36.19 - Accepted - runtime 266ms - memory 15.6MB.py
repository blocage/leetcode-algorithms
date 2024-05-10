class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == '*':
                res.pop()
            else:
                res += [i]
        
        return ''.join(res)