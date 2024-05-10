class Solution:
    def reformat(self, s: str) -> str:
        a = b = ''
        for i in s:
            if i.isalpha():a += i
            else:b += i
        if abs(len(a) - len(b)) > 1: return ''
        a, b = sorted((a,b),key=len)
        r = ''.join(i+j for i,j in zip(b,a))
        if len(a) != len(b):
            r += b[-1]
        return r
