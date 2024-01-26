class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else (math.log10(n) / math.log10(4)) % 1 == 0