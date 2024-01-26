class Solution:
    def sumBase(self, n: int, k: int) -> int:
        return self.sumBase(n // k, k) + n % k if n else 0