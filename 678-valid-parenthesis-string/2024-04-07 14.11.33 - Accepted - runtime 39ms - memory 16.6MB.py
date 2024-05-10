class Solution:
    def checkValidString(self, s: str) -> bool:
        a = b = 0
        for i in s:
            a = a - 1 if i == ')' else a + 1
            b = b + 1 if i == '(' else max(b - 1, 0)
            if a < 0: return False
        

        return b == 0