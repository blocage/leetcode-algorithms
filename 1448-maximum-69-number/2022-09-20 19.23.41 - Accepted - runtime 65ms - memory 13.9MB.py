class Solution:
    def maximum69Number(self, num: int) -> int:
        l = list(str(num))
        if '6' in l:
            l[l.index('6')] = '9'
        return ''.join(l)