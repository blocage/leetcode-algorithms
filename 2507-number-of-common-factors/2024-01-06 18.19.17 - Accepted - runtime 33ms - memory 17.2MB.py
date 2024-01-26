class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(a % f == 0 and b % f == 0 for f in range(1, max(a,b) + 1))
        