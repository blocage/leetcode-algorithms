class Solution:
    def countAndSay(self, n: int) -> str:
        t = 1
        res = '1'
        while t < n:
            tmp = ''
            for a,b in groupby(res):
                tmp += f'{len(list(b))}{a}'
            res = tmp
            t += 1
        return res