class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y: x, y = y, x
        x, y = map(lambda x: bin(x)[2:], (x, y))
        x = x.zfill(l := len(y))
        return sum(x[f] != y[f] for f in range(l))