class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        r = ''
        op = 0
        for i in s:
            if i == '(':
                op += 1
                r += i

            elif i == ')':
                if op:
                    r += i
                    op -= 1
            
            else:
                r += i
            

        return r[::-1].replace('(', '', op)[::-1]