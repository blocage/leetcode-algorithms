class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else (math.log10(n) / math.log10(3)) % 1 == 0
        