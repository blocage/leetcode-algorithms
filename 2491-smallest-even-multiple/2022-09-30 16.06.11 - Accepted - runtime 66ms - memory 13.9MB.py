class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n + n if n % 2 else n