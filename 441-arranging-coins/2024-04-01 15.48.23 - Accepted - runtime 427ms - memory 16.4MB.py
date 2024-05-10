class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 0
        while True:
            if n < r:
                return r - 1
            n -= r
            r += 1