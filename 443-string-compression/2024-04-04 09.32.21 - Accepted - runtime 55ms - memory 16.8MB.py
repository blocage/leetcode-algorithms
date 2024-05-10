class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        r = []
        for a,b in groupby(chars):
            b = len(list(b))
            r.append(a)
            res += 1
            if b > 1:
                res += len(str(b))
                r += list(str(b))
        
        chars[:] = r
        return res