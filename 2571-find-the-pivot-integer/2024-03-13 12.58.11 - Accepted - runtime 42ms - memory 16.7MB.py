class Solution:
    def pivotInteger(self, n: int) -> int:
        n *= (n + 1) / 2
        x = int(n ** .5)
        return x if x * x == n else -1