_min = -(2 ** 31)
_max = abs(_min) - 1
class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = int(str(abs(x))[::-1])
        if neg:
            x = -x
        return x if _min <= x <= _max else 0