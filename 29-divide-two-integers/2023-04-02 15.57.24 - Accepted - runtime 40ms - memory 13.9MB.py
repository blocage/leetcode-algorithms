HI = 2 ** 31 - 1
LO = -2 ** 31
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        s = int(dividend / divisor)
        return min(max(s, LO), HI)